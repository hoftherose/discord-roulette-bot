from typing import Self
from sqlalchemy import Column, String
from sqlalchemy import select, insert, update, delete

from src.utils.logger import logger
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
    async def get_by_id(cls, user_id: str) -> Self:
        async with Session() as session:
            return await session.get(cls, user_id)

    async def create(self) -> None:
        async with Session() as session:
            session.add(self)
            await session.commit()
            logger.info(f"User {self.id} created")

    async def change_name(self, name: str):
        async with Session() as session:
            session.add(self)
            old_name = self.name
            self.name = name
            await session.commit()
            logger.info(f"User {self.id} name changed from {old_name} to {name}")

    @classmethod
    async def delete(cls, user: Self):
        async with Session() as session:
            await session.delete(user)
            await session.commit()
            logger.info(f"User {user.id} deleted from database")
