from typing import List
from sqlalchemy import (
    String,
)
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.models import Base, Address


class User(Base):
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str | None]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
