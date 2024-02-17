from fastapi import APIRouter
from src.services.users import (
    get_all_users,
    get_users,
    create_user,
    update_user,
    remove_user,
)

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def list_users():
    users = await get_all_users()
    return users


@router.get("/{user_id}")
async def read_user(user_id: str):
    user = await get_users([user_id])
    return user


@router.post("/{user_id}")
async def post_user(user_id: str, name: str):
    await create_user(user_id, name)
    return {"msg": f"User {user_id} successfully created"}


@router.patch("/{user_id}")
async def patch_user(user_id: str):
    user = await update_user(user_id)
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    await remove_user(user_id)
    return {"msg": f"User {user_id} successfully deleted"}
