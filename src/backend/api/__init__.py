from fastapi import APIRouter, Depends

from backend.core.config import settings
from backend.deps.auth import get_query_token

from .routers.user import user_router

routers = APIRouter(prefix=settings.api_prefix)

routers.include_router(user_router, dependencies=[Depends(get_query_token)])
