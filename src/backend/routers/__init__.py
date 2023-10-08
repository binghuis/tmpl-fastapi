from fastapi import APIRouter, Depends
from backend.config import settings
from backend.deps.auth import get_query_token

from .user_router import user_router

root_router = APIRouter(prefix=settings.API_PREFIX)

root_router.include_router(user_router, dependencies=[Depends(get_query_token)])
