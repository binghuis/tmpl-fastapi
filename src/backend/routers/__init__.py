from fastapi import APIRouter, Depends
from backend.config.settings import settings
from backend.utils.auth import get_token_header

from backend.internal import admin
from . import items, users

router = APIRouter(prefix=settings.ROOT_PATH)

router.include_router(users.router)
router.include_router(items.router)
router.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)
