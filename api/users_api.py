# api/cars_api.py
import fastapi
from typing import List
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from models import users_models
from schema import users_schema
from databases.database import SessionLocal

router = fastapi.APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/user')
def create_user(request: users_schema.User, db: Session = Depends(get_db)):
    new_user = users_models.User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user