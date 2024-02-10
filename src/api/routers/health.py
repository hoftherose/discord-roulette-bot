from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Server"])


@router.get("/")
def health_check():
    return {"status": "up"}
