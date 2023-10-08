from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models import user_model, address_model
from backend.schemas import user_schema


def get_user(session: Session, user_id: int):
    stmt = select(user_model.User).filter(user_model.User.id == user_id)
    return session.execute(statement=stmt).first()


def get_user_by_email(session: Session, name: str):
    stmt = select(user_model.User).filter(user_model.User.fullname == name)
    return session.execute(stmt).first()


def get_users(session: Session, skip: int = 0, limit: int = 100):
    stmt = select(user_model.User).offset(skip).limit(limit)
    return session.execute(stmt).all()


def create_user(session: Session, user: user_schema.UserCreate):
    address = [address_model.Address()]
    session.add(user)
    session.commit()
    return user
