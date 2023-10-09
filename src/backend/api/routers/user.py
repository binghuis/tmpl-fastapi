from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import APIRouter, Depends, status, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.user import User
from backend.api.schemas.user import UserSchema, UserResponse, UserLogin, TokenResponse


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    payload: UserSchema, request: Request, db_session: AsyncSession = Depends(get_db)
):
    _user: User = User(**payload.model_dump())
    await _user.save(db_session)

    # TODO: add refresh token
    _user.access_token = await create_access_token(_user, request)
    return _user


@user_router.post(
    "/token", status_code=status.HTTP_201_CREATED, response_model=TokenResponse
)
async def get_token_for_user(
    user: UserLogin, request: Request, db_session: AsyncSession = Depends(get_db)
):
    _user: User = await User.find(db_session, [User.email == user.email])

    # TODO: out exception handling to external module
    if not _user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not _user.check_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
        )

    # TODO: add refresh token
    _token = await create_access_token(_user, request)
    return {"access_token": _token, "token_type": "bearer"}
