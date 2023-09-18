from datetime import datetime
from typing import List
from sqlalchemy import (
    DateTime,
    Integer,
    String,
    Text,
    create_engine,
    func,
    UniqueConstraint,
    ForeignKey,
)
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.db.client import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str | None]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"User(id={self.id!r}, name={self.name!r}), username={self.username!r}"

    def __repr__(self) -> str:
        return str(self)


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
