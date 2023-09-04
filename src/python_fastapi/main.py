from enum import Enum
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field
from uuid import UUID

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


@app.get("/users")
async def read_users(
    *,
    page_size: Annotated[int, Query(description="每页条数", ge=10)] = 10,
    page_index: Annotated[int, Query(description="索引", gt=1)] = 1,
):
    results = {"page_index": page_index, "page_size": page_size}
    return results


@app.get("/users/{id}")
async def read_user(id: Annotated[UUID, Path(description="用户 ID")]):
    return {"id": id}


class UserDetail(BaseModel):
    address: str = Field(examples=["家庭地址"])


class User(BaseModel):
    name: str
    age: int = Field(ge=1, description="年龄")
    detail: UserDetail = Field()


@app.post("/users/create")
async def create_user(user: Annotated[User, Body()]):
    return user


@app.put("/users/{id}")
async def update_user(id: Annotated[UUID, Path()], user: Annotated[User, Body()]):
    return {"id": id, **user.model_dump()}
