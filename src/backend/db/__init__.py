from sqlalchemy import create_engine
from backend.config import settings
from backend.models import Base


engine = create_engine(settings.DB_URI, echo=settings.ECHO_SQL)

Base.metadata.create_all(bind=engine)
