import asyncio
from src.repo.db import Users


def get_all_users() -> list[Users]:
    return asyncio.run(Users.get_all())


def get_user_by_id(user_id: str) -> Users:
    return asyncio.run(Users.get_by_id(user_id))


def create_user(user_id: str, name: str) -> None:
    user = Users(id=user_id, name=name)
    asyncio.run(user.create())


def change_user_name(user_id: str, name: str) -> None:
    users = asyncio.run(get_user_by_id(user_id))
    asyncio.run(users.change_name(name=name))


def remove_user(user_id: str) -> None:
    user = asyncio.run(get_user_by_id(user_id))
    asyncio.run(Users.delete(user))
