from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from backend.api.schemas.user import User, UserCreate
from backend.services.user import get_user, get_user_by_email, get_users


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/", response_model=User)
def create_user(user: UserCreate):
    with Session as session:
        db_user = get_user_by_email(session, email=user.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        return create_user(session=session, user=user)


@user_router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100):
    with Session as session:
        users = get_users(session=session, skip=skip, limit=limit)
        return users


@user_router.get("/{user_id}", response_model=User)
def read_user(user_id: int):
    with Session as session:
        db_user = get_user(session, user_id=user_id)
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return db_user
