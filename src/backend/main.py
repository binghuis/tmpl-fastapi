from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, Request, Response, status

from backend.config import settings
from backend.db.client import SessionLocal

from backend.routers import root_router

app = FastAPI()

app.include_router(root_router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response(
        "Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


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
