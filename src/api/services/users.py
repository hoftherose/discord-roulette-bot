from src.api.repo.db import Users


def get_all_users() -> list[Users]:
    users = Users.get_all()
    return {user.id: {"name": user.name} for user in users}


def get_users(user_ids: list[str]) -> Users:
    users = Users.get_by_ids(user_ids)
    return {user.id: {"name": user.name} for user in users}


def create_user(user_id: str, name: str) -> Users:
    user = Users(user_id, "John")
    user.create()
    return {user.id: {"name": user.name}}


def update_user(user_id: str, name: str) -> Users:
    user = get_users([user_id])
    user.name = name
    user.update(name=name)
    return {user.id: {"name": user.name}}


def remove_user(user_id: str) -> None:
    user = Users.get_by_ids([user_id])
    Users.delete(user_id)
