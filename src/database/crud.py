from sqlalchemy.orm import Session

from src.database import models
from src.schemas.prediction_schemas import PredictionCreate
from src.schemas.user_schemas import SignUp


def get_user(user_id: int, db: Session):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(username: str, db: Session):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(user: SignUp, db: Session):
    db_user = models.User(
        username=user.username, fullname=user.fullname, password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_balance(user_id: int, updated_balance: int, db: Session):
    db.query(models.User).filter(models.User.id == user_id).update(
        {"balance": updated_balance}
    )
    db.commit()


def create_prediction(pred: PredictionCreate, user_id: int, db: Session):
    db_prediction = models.Prediction(**pred.model_dump(), owner_id=user_id)
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction


def get_user_predictions(user_id: int, db: Session):
    return (
        db.query(models.Prediction).filter(models.Prediction.owner_id == user_id).all()
    )
