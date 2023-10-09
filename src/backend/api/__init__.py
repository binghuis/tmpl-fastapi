from fastapi import APIRouter, Depends
from backend.core.settings import settings
from backend.deps.auth import get_query_token

from .routers.user import user_router

routers = APIRouter(prefix=settings.API_PREFIX)

routers.include_router(user_router, dependencies=[Depends(get_query_token)])
