# /home/lenovo/Videos/hackathon-project/backend/crud.py
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from auth import get_password_hash


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
