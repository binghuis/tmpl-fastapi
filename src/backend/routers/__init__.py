from fastapi import APIRouter, Depends
from backend.settings import settings

from .user.router import user_router

root_router = APIRouter(prefix=settings.ROOT_PATH)

root_router.include_router(user_router)
