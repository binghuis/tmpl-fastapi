from typing import Any

import bcrypt
from passlib.context import CryptContext
from sqlalchemy import LargeBinary, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class User(Base):
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    _password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    @property
    def password(self):
        return self._password.decode('utf-8')

    @password.setter
    def password(self, password: str):
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password: str):
        return pwd_context.verify(password, self.password)

    @classmethod
    async def find(cls, database_session: AsyncSession, where_conditions: list[Any]):
        _stmt = select(cls).where(*where_conditions)
        _result = await database_session.execute(_stmt)
        return _result.scalars().first()
