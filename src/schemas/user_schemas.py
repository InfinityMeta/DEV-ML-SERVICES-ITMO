from pydantic import BaseModel

from src.schemas.prediction_schemas import Prediction


class UserBase(BaseModel):
    username: str


class SignIn(UserBase):
    password: str


class SignUp(UserBase):
    fullname: str
    password: str


class User(UserBase):
    id: int
    fullname: str
    balance: float
    predictions: list[Prediction] = []

    class Config:
        from_attributes = True
