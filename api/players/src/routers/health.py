from fastapi import APIRouter
from src.utils.logger import logger

router = APIRouter(prefix="/health", tags=["Server"])


@router.get("/")
def health_check():
    logger.info("Checking health")
    return {"status": "up"}
