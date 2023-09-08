import secrets
from typing import Any, Callable, Dict, List, Optional, Set, Union

from pydantic import AnyHttpUrl, Field, PostgresDsn, AnyUrl, FileUrl

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ROOT_PATH: str = "/api"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: Set[AnyHttpUrl] = []
    SQLALCHEMY_DATABASE_URL: str = "postgresql://localhost"
