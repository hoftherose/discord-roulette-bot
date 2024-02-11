from typing import Self
from src.api.repo.conn import Base, session
from sqlalchemy import Column, String

class Users(Base):
    __tablename__ = "bas_ficax_services_view"

    user_id = Column("USER_ID", String(20), primary_key=True)
    name = Column("NAME", String(50))

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
