from sqlalchemy import (
    ForeignKey,
)
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.models import Base, user


class Address(Base):
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["user.User"] = relationship(back_populates="addresses")
