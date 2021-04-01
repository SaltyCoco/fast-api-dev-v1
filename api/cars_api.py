# api/cars_api.py
import fastapi
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from models import cars_models
from schema import cars_schema
from databases.database import SessionLocal

router = fastapi.APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/cars')
def create_car(request: cars_schema.Car, db: Session = Depends(get_db)):
    new_car = cars_models.Car(
        make=request.make,
        model=request.model,
        year_of_manufacture=request.year_of_manufacture,
        miles=request.miles,
        condition_value=request.condition_value,
        color=request.color,
        price=request.price
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


@router.get('/cars')
def get_all_cars(db: Session = Depends(get_db)):
    cars = db.query(cars_models.Car).all()
    return cars