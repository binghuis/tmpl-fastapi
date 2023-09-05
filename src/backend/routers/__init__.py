from fastapi import APIRouter, Depends
from backend.dependencies import get_token_header

from backend.internal import admin
from . import items, users

router = APIRouter(prefix="/api")

router.include_router(users.router)
router.include_router(items.router)
router.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)
