from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    username: str
    emails: list[str] | None


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
