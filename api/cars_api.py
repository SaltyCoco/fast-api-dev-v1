# api/cars_api.py
import fastapi
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import api.car_status_api
import schema.cars_schema
from models.cars_models import Car as model_car
from databases.database import SessionLocal

router = fastapi.APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_cars(db: SessionLocal, skip: int = 0, limit: int = 100):
    return db.query(model_car).offset(skip).limit(limit).all()


@router.get("/cars/", response_model=List[model_car])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = get_cars(db, skip=skip, limit=limit)
    return cars
