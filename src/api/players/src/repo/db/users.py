from typing import Self
from sqlalchemy import Column, String
from sqlalchemy import select, insert, update, delete

from src.repo.conn import Base, Session


class Users(Base):
    __tablename__ = "users"

    id = Column("USER_ID", String(20), primary_key=True)
    name = Column("NAME", String(50))

    @classmethod
    async def get_all(cls) -> list[Self]:
        async with Session() as session:
            results = await session.execute(select(cls))
            return [result[0] for result in results]

    @classmethod
    async def get_by_id(cls, user_ids: str) -> Self:
        async with Session() as session:
            return await session.get(cls, user_ids)

    async def create(self) -> None:
        async with Session() as session:
            session.add(self)
            await session.commit()

    async def change_name(self, name: str):
        async with Session() as session:
            session.add(self)
            self.name = name
            await session.commit()

    async def delete(self):
        async with Session() as session:
            await session.delete(self)
