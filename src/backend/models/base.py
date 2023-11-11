import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}_table'

    def __repr__(self) -> str:
        columns = ', '.join(
            [
                f'{k}={repr(v)}'
                for k, v in self.__dict__.items()
                if not k.startswith('_')
            ]
        )
        return f'<{self.__class__.__name__}({columns})>'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), default=uuid.uuid4, primary_key=True
    )
