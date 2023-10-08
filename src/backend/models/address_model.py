from sqlalchemy import (
    ForeignKey,
)
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.models import Base, User


class Address(Base):
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")
