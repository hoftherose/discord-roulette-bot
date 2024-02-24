from fastapi import APIRouter

from src.utils.logger import logger
from src.services.users import (
    get_all_users,
    get_user_by_id,
    create_user,
    change_user_name,
    remove_user,
)

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def list_users():
    users = await get_all_users()
    return users


@router.get("/{user_id}")
async def get_user(user_id: str):
    user = await get_user_by_id(user_id)
    return user


@router.post("/{user_id}")
async def post_user(user_id: str, name: str):
    await create_user(user_id, name)
    return {"msg": f"User {user_id} successfully created"}


@router.patch("/{user_id}/name")
async def update_user_name(user_id: str, name: str):
    await change_user_name(user_id, name)
    return {"msg": f"User {user_id} name changed to {name}"}


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    await remove_user(user_id)
    return {"msg": f"User {user_id} successfully deleted"}
