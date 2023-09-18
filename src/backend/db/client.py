from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from backend.config import settings
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.SQLALCHEMY_URL, echo=settings.SQLALCHEMY_ECHO)

Base.metadata.create_all(bind=engine)
