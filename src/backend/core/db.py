from sqlalchemy import create_engine
from backend.core.settings import settings
from backend.models import Base


Base.metadata.create_all(bind=engine)


from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.utils.logging import AppLogger

logger = AppLogger.__call__().get_logger()

engine = create_async_engine(settings.DB_URI, echo=settings.ECHO_SQL)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)


# Dependency
async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        yield session
