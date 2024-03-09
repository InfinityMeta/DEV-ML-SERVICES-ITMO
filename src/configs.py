from datetime import timedelta

import joblib
from passlib.context import CryptContext

# ======> Registration <======
DEFAULT_CREDITS = 50.0

# ======> Authentication <======
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
HASHING_ALGORITHM = "HS256"
TOKEN_EXPIRES_DELTA = timedelta(minutes=15)

# ======> Prediction <======
FEATURES = {
    "temperature",
    "humidity",
    "CO2CosIRValue",
    "CO2MG811Value",
    "MOX1",
    "MOX2",
    "MOX3",
    "MOX4",
    "COValue",
    "inhabited",
    "hour",
}

PREPROCESSING_MODELS = {
    "pca": (3, joblib.load("models/pca.joblib")),
}

PREDICTION_MODELS_COSTS = {
    "sklearn_gb": 15,
    "catboost": 7,
    "random_forest": 5,
}

PREDICTION_MODELS = {
    "sklearn_gb": joblib.load("models/sklearn_gb.joblib"),
    "catboost": joblib.load("models/catboost.joblib"),
    "random_forest": joblib.load("models/random_forest.joblib"),
}

ANOMALY_THRESHOLDS = {"danger": 0.8, "warning": 0.5}

BROKER_URL = "redis://localhost:6379/0"
BROKER_BACKEND = "redis://localhost:6379/0"
