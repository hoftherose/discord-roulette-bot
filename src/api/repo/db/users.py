from typing import Self


class Users:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    @classmethod
    def get_all(cls) -> list[Self]:
        return cls("1", "John")

    @classmethod
    def get_by_ids(cls, user_ids: str) -> list[Self]:
        return [cls(user_id, "John") for user_id in user_ids]

    def create(self):
        pass

    def update(self, **args):
        pass

    def delete(self):
        pass
