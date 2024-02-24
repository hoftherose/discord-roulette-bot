from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import health_checker_router, user_router
from src.repo.conn import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["Content-Type"],
    allow_credentials="true",
)

app.include_router(user_router)
app.include_router(health_checker_router)
