from sqlalchemy import create_engine

from backend.core.config import settings
from backend.models.base import Base

engine = create_engine(
    settings.db_url,
    echo=settings.echo_sql,
    future=True,
)

Base.metadata.create_all(bind=engine)


class DB:
    pass
