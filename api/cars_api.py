# api/cars_api.py
import fastapi
from typing import List
from fastapi import Depends, status
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


@router.post('/cars', status_code=status.HTTP_201_CREATED)
async def create_car(request: cars_schema.Car, db: Session = Depends(get_db)):
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
async def get_all_cars(db: Session = Depends(get_db)):
    cars = db.query(cars_models.Car).all()
    return cars


@router.get('/cars/{id}')
async def get_car_by_id(id, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.id == id).first()
    return car


@router.get('/cars/model/{model}')
async def get_car_by_model(model, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.model == model).all()
    return car


@router.get('/cars/make/{make}')
async def get_car_by_make(make, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.make == make).all()
    return car


@router.get('/cars/yom/{year_of_manufacture}')
async def get_car_by_year_of_manufacture(year_of_manufacture, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.year_of_manufacture == year_of_manufacture).all()
    return car
