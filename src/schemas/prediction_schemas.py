from datetime import datetime

from pydantic import BaseModel


class PredictionBase(BaseModel):
    modelname: str
    prediction: str
    balance_shift: float


class PredictionCreate(PredictionBase):
    pass


class Prediction(PredictionBase):
    id: int
    creation_date: datetime
    owner_id: int

    class Config:
        from_attributes = True
