from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, registry
from backend.config import settings
from sqlalchemy.schema import MetaData

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

reg = registry()


class Base(DeclarativeBase):
    registry = reg


MetaData().create_all(bind=engine)
