from src.repo.db import Users


async def get_all_users() -> list[Users]:
    return await Users.get_all()


async def get_users_by_id(user_id: str) -> Users:
    return await Users.get_by_id(user_id)


async def create_user(user_id: str, name: str) -> None:
    user = Users(id=user_id, name=name)
    await user.create()


async def change_user_name(user_id: str, name: str) -> None:
    users = await get_users_by_id(user_id)
    await users.change_name(name=name)


async def remove_user(user_id: str) -> None:
    user = await get_users_by_id(user_id)
    await Users.delete(user)
