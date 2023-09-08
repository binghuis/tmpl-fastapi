from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI

from .config.settings import settings

from backend.deps.auth import get_query_token
from backend.routers import root_router

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(root_router)


if len(settings.BACKEND_CORS_ORIGINS) > 0:
    app.add_middleware(
        CORSMiddleware,
        allow_headers=["*"],
        allow_methods=["*"],
        allow_credentials=False,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_origin_regex="",
        max_age=600,
        expose_headers=[],
    )


@app.get("/")
async def root():
    return "hello world"
