from fastapi import FastAPI
from src.api.routers import health_checker_router, user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(health_checker_router)
