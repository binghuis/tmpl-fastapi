import secrets
from typing import ClassVar, Set

from pydantic import HttpUrl

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: ClassVar[str] = "/api"
    SECRET_KEY: ClassVar[str] = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: ClassVar[int] = 60 * 24 * 8
    # CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    CORS_ORIGINS: ClassVar[Set[HttpUrl]] = []
    # DB_URI = "postgresql://localhost"
    DB_URI: ClassVar[str] = "sqlite:///./sql_app.db"
    ECHO_SQL: ClassVar[bool] = True


settings = Settings()
