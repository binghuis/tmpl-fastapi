from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from backend.core.settings import settings

from backend.api import routers

app = FastAPI()

app.include_router(routers)


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


@app.get("/")
async def health() -> JSONResponse:
    return JSONResponse({"message": "It worked!!"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
