# api/cars_api.py

import fastapi
from typing import List
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from models import users_models
from schema import users_schema
from databases.database import SessionLocal
from .hashing import Hash

router = fastapi.APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=users_schema.ShowUser, tags=['Users'])
async def create_user(request: users_schema.User, db: Session = Depends(get_db)):
    new_user = users_models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=users_schema.ShowUser, tags=['Users'])
async def get_user(id, db: Session = Depends(get_db)):
    user = db.query(users_models.User).filter(users_models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No users with that id.")
    return user
