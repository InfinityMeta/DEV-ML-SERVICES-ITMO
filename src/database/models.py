from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.configs import DEFAULT_CREDITS
from src.database.core import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    balance = Column(Float, default=DEFAULT_CREDITS)
    predictions = relationship("Prediction", back_populates="owner")


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime, default=datetime.now)
    modelname = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
    balance_shift = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="predictions")
