from src.api.repo.db import Users


def get_all_users() -> list[Users]:
    return Users.get_all()


def get_users(user_ids: list[str]) -> Users:
    return Users.get_by_ids(user_ids)


def create_user(user_id: str, name: str) -> Users:
    user = Users(user_id, "John")
    return user.create()


def update_user(user_id: str, name: str) -> Users:
    user = get_users([user_id])
    user.name = name
    return user.update()


def remove_user(user_id: str) -> None:
    user = Users.get_by_ids([user_id])
    return Users.delete(user)
