from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.database.core import get_db
from src.schemas.sensors_schemas import Sensor
from src.schemas.user_schemas import User
from src.services.auth_service import get_current_user
from src.services.predict_service import (check_prediction, get_prediction_id,
                                          get_user_info)

router = APIRouter()


@router.post("/models/{modelname}/predict")
def send_data_for_prediction(
    modelname: str,
    sensor_values: Sensor,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    prediction_id = get_prediction_id(modelname, user.username, sensor_values, db)
    return JSONResponse({"prediction_id": prediction_id})


@router.get("/models/{modelname}/predictions/{prediction_id}")
def get_prediction(
    modelname: str,
    prediction_id: str,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    result = check_prediction(prediction_id, modelname, user.username, db)
    return result


@router.get("/users/user_history", response_model=User)
def get_user_predictions_history(
    user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return get_user_info(user, db)
