from fastapi import FastAPI
from src.routers import health_checker_router

app = FastAPI()

app.include_router(health_checker_router)