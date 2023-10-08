from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from backend.config import settings

from backend.routers import root_router

app = FastAPI()

app.include_router(root_router)


if len(settings.CORS_ORIGINS) > 0:
    app.add_middleware(
        CORSMiddleware,
        allow_headers=["*"],
        allow_methods=["*"],
        allow_credentials=False,
        allow_origins=settings.CORS_ORIGINS,
        allow_origin_regex="",
        max_age=600,
        expose_headers=[],
    )
