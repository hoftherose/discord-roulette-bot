from fastapi import FastAPI
from src.routers import health_checker_router, user_router
from src.repo.conn import Base

app = FastAPI()

app.include_router(user_router)
app.include_router(health_checker_router)
