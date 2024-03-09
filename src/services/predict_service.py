import time

import numpy as np
import pandas as pd
from celery import Celery
from celery.result import AsyncResult
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.configs import (ANOMALY_THRESHOLDS, BROKER_BACKEND, BROKER_URL,
                         FEATURES, PREDICTION_MODELS, PREDICTION_MODELS_COSTS,
                         PREPROCESSING_MODELS)
from src.database import crud
from src.schemas.prediction_schemas import PredictionCreate
from src.schemas.sensors_schemas import Sensor
from src.schemas.user_schemas import User

celery_app = Celery(__name__)
celery_app.conf.broker_url = BROKER_URL
celery_app.conf.result_backend = BROKER_BACKEND
celery_app.conf.broker_connection_retry_on_startup = True


def _validate_data(sensor_values: Sensor):
    features = pd.Series(sensor_values.model_dump())
    for feature, value in features.items():
        if type(value) not in [float, int]:
            raise ValueError(f"{feature} : not a number received")
        if value < 0:
            raise ValueError(f"{feature} : must be nonnegative")
    if features["inhabited"] not in [0, 1]:
        raise ValueError("inhabited is binary: 1 - inhabited, 0 - uninhabited")
    if features["hour"] not in list(range(24)):
        raise ValueError("Incorrect hour")


def _preprocess_data(sensor_values: Sensor):
    features = pd.Series(sensor_values.model_dump())
    if set(features.index) != FEATURES:
        raise ValueError("Wrong features set")
    pca_features = ["MOX2", "MOX3", "MOX4"]
    _, pca = PREPROCESSING_MODELS["pca"]
    pca_result = pca.transform(features[pca_features].values.reshape(1, -1))
    features.drop(pca_features, inplace=True)
    features["MOX_ADD"] = pca_result[0][0]
    return np.array(features).reshape(1, -1)


def get_prediction_id(
    modelname: str, username: str, sensor_values: Sensor, db: Session
):
    try:
        _validate_data(sensor_values)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    db_user = crud.get_user_by_username(username=username, db=db)
    model_cost = PREDICTION_MODELS_COSTS[modelname]
    if db_user.balance < model_cost:
        raise HTTPException(status_code=402, detail="Not enough money")
    prediction_task = make_prediction.delay(sensor_values.model_dump_json(), modelname)
    return prediction_task.id


def check_prediction(prediction_id: str, modelname: str, username: str, db: Session):
    prediction = AsyncResult(prediction_id, app=celery_app)

    if prediction.failed():
        raise HTTPException(status_code=400, detail=str(prediction.result))

    if not prediction.ready():
        return {
            "prediction_status": prediction.status,
        }

    anomaly_prob = prediction.result
    db_user = crud.get_user_by_username(username=username, db=db)
    model_cost = PREDICTION_MODELS_COSTS[modelname]
    balance_shift = -model_cost
    db_user.balance -= model_cost
    crud.update_user_balance(db_user.id, db_user.balance, db=db)

    if anomaly_prob >= ANOMALY_THRESHOLDS["danger"]:
        return_message = "DANGER"
    elif anomaly_prob >= ANOMALY_THRESHOLDS["warning"]:
        return_message = "WARNING"
    else:
        return_message = "OK"

    pred = PredictionCreate(
        prediction=return_message,
        modelname=modelname,
        balance_shift=balance_shift,
    )
    crud.create_prediction(pred, db_user.id, db=db)
    result = {
        "prediction_status": prediction.status,
        "prediction_result": return_message,
    }
    return result


def get_user_info(user: User, db: Session):
    return crud.get_user_by_username(user.username, db)


@celery_app.task(time_limit=30)
def make_prediction(sensor_values, modelname):
    time.sleep(10)  # for checking queue work
    sensor_values = Sensor(**eval(sensor_values))
    preprocessed_features = _preprocess_data(sensor_values)
    model = PREDICTION_MODELS[modelname]
    _, anomaly_prob = model.predict_proba(preprocessed_features)[0]
    return anomaly_prob
