from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database.core import get_db
from src.schemas.token_schemas import Token
from src.schemas.user_schemas import SignIn, SignUp, User
from src.services.auth_service import login_for_access_token, sign_up_user

router = APIRouter()


@router.post("/token", response_model=Token)
def sign_in(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = SignIn(username=user.username, password=user.password)
    return login_for_access_token(user, db)


@router.post("/sign-up", response_model=User)
def sign_up(user: SignUp, db: Session = Depends(get_db)):
    return sign_up_user(user, db)
