from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI

from .dependencies import get_query_token
from backend.routers import router

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=False,
    allow_origins=["*"],
    allow_origin_regex="",
    max_age=600,
    expose_headers=[],
)


@app.get("/")
async def root():
    return "hello world"