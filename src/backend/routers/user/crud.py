from sqlalchemy import select
from sqlalchemy.orm import Session

from . import model, schema


def get_user(session: Session, user_id: int):
    stmt = select(model.User).filter(model.User.id == user_id)
    return session.execute(statement=stmt).first()


def get_user_by_email(session: Session, name: str):
    stmt = select(model.User).filter(model.User.fullname == name)
    return session.execute(stmt).first()


def get_users(session: Session, skip: int = 0, limit: int = 100):
    stmt = select(model.User).offset(skip).limit(limit).all()
    return session.scalar(stmt)


def create_user(session: Session, user: schema.UserCreate):
    address = [model.Address()]
    session.add(user)
    session.commit()
    return user
