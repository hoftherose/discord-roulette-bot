from fastapi import APIRouter
from src.api.services.users import get_all_users, get_users, create_user, update_user, remove_user

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
def list_users():
    users = get_all_users()
    return users

@router.get("/{user_id}")
def read_user(user_id: str):
    user = get_users([user_id])
    return user

@router.post("/{user_id}")
def post_user(user_id: str):
    user = create_user(user_id)
    return user

@router.patch("/{user_id}")
def patch_user(user_id: str):
    user = update_user(user_id)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: str):
    remove_user(user_id)
    return {"msg": f"User {user_id} successfully deleted"}
