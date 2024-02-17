from src.repo.db import Users


async def get_all_users() -> list[Users]:
    return await Users.get_all()


async def get_users(user_ids: list[str]) -> Users:
    return await Users.get_by_ids(user_ids)


async def create_user(user_id: str, name: str) -> Users:
    user = Users(user_id, "John")
    return await user.create()


async def update_user(user_id: str, name: str) -> Users:
    user = await get_users([user_id])
    user.name = name
    return await user.update()


async def remove_user(user_id: str) -> None:
    user = await Users.get_by_ids([user_id])
    return await Users.delete(user)
