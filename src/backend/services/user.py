from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models import address, user
from backend.api.schemas.user import UserCreate


def get_user(session: Session, user_id: int):
    stmt = select(user.User).filter(user.User.id == user_id)
    return session.execute(statement=stmt).first()


def get_user_by_email(session: Session, name: str):
    stmt = select(user.User).filter(user.User.fullname == name)
    return session.execute(stmt).first()


def get_users(session: Session, skip: int = 0, limit: int = 100):
    stmt = select(user.User).offset(skip).limit(limit)
    return session.execute(stmt).all()


def create_user(session: Session, user: UserCreate):
    address = [address.Address()]
    session.add(user)
    session.commit()
    return user
