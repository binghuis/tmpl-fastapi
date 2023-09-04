from enum import Enum
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Fastapi Demo")

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
def read_root():
    return "Hello World"


@app.get("/users")
async def read_users(
    *,
    page_size: Annotated[int, Query(description="每页条数", ge=10)] = 10,
    page_index: Annotated[int, Query(description="索引", gt=1)] = 1,
):
    results = {"page_index": page_index, "page_size": page_size}
    return results


@app.get("/users/{id}")
async def read_user(id: Annotated[int, Path(description="用户 ID")]):
    return {"id": id}


class UserDetail(BaseModel):
    address: str = None


class User(BaseModel):
    name: str = Field(examples=["李华"])
    age: int = Field(examples=[16])
    detail: UserDetail = Field()
    model_config = {
        "json_schema_extra": {"examples": [{name: "李华", age: 16, detail: {}}]}
    }


@app.post("/users/create")
async def create_user(user: User):
    return user


@app.put("/users/{id}")
async def update_user():
    pass
