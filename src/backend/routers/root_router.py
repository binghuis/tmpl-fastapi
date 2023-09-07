from fastapi import APIRouter, Depends
from backend.settings import settings
from backend.utils.auth import get_token_header

from backend.internal import admin
from .user.router import user_router

root_router = APIRouter(prefix=settings.ROOT_PATH)

root_router.include_router(user_router)
root_router.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)
