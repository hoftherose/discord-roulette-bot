from fastapi import APIRouter
from src.utils.logger import logger

router = APIRouter(prefix="/health", tags=["Server"])


@router.get("/")
def health_check():
    ok_status = {"status": "up"}
    logger.info(f"Current health: {ok_status}")
    return ok_status
