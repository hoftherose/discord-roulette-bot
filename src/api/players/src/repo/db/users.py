from typing import Self
from sqlalchemy import Column, String
from sqlalchemy import select, insert, update, delete

from src.repo.conn import Base

class Users(Base):
    __tablename__ = "user"

    id = Column("USER_ID", String(20), primary_key=True)
    name = Column("NAME", String(50))

    @classmethod
    def get_all(cls) -> list[Self]:
        return select(cls).all()

    @classmethod
    def get_by_ids(cls, user_ids: list[str]) -> list[Self]:
        return select(cls).where(cls.id.in_(user_ids)).all()

    def create(self):
        return insert(self)

    def update(self):
        return update(self)

    def delete(self):
        return delete(self)
