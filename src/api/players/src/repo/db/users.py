from typing import Self
from sqlalchemy import Column, String
from sqlalchemy import select, insert, update, delete

from src.repo.conn import Base, Session


class Users(Base):
    __tablename__ = "user"

    id = Column("USER_ID", String(20), primary_key=True)
    name = Column("NAME", String(50))

    @classmethod
    async def get_all(cls) -> list[Self]:
        async with Session() as session:
            result = await session.execute(select(cls))
            return result.all()

    @classmethod
    async def get_by_ids(cls, user_ids: list[str]) -> list[Self]:
        async with Session() as session:
            result = await session.execute(select(cls).where(cls.id.in_(user_ids)))
            return result.all()

    async def create(self):
        async with Session() as session:
            session.add(self)

    async def update(self):
        return update(self)

    async def delete(self):
        return delete(self)
