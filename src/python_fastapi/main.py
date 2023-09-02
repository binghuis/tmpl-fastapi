from enum import Enum
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(title="Fastapi Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex="",
    expose_headers=[],
    max_age=600,
)


@app.get("/")
def read_root():
    return "Hello World"


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(description="通过 id 获取 item")],
    q: Annotated[str, Query(alias="item-query", description="查询参数 q")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
