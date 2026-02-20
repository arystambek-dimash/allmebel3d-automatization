from typing import Any

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class DatabaseConnection:
    def __init__(
            self,
            db_uri: str,
            echo: bool = False,
    ) -> None:
        self.db_uri = db_uri
        self.echo = echo
        self.create_session()

    def create_session(self) -> async_sessionmaker[AsyncSession | Any]:
        session = async_sessionmaker(
            bind=self._engine,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
        )
        return session

    def _create_engine(self):
        self._engine = create_async_engine(
            url=self.db_uri,
            echo=self.echo,
        )

    async def close(self) -> None:
        await self._engine.dispose()


class Base(DeclarativeBase):
    ...
