import secrets
from typing import Any, Callable, ClassVar, Dict, List, Optional, Set, Union

from pydantic import AnyHttpUrl, Field, PostgresDsn, AnyUrl, FileUrl

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ROOT_PATH: ClassVar[str] = "/api"
    SECRET_KEY: ClassVar[str] = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: ClassVar[int] = 60 * 24 * 8
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: ClassVar[Set[AnyHttpUrl]] = []
    # SQLALCHEMY_URL = "postgresql://localhost"
    SQLALCHEMY_URL: ClassVar[str] = "sqlite:///./sql_app.db"
    SQLALCHEMY_ECHO: ClassVar[bool] = True
