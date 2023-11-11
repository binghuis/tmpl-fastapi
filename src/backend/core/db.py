from sqlalchemy import create_engine

from backend.core.config import settings
from backend.models import Base

engine = create_engine(
    settings.DB_URI,
    echo=settings.ECHO_SQL,
    future=True,
)

Base.metadata.create_all(bind=engine)
