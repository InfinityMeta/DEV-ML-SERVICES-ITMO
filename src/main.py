from fastapi import FastAPI

from src.database import core
from src.endpoints.auth_endpoints import router as auth_router
from src.endpoints.predict_endpoints import router as predict_router

core.Base.metadata.create_all(bind=core.engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(predict_router)
