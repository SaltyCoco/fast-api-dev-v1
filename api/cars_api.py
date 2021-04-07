# api/cars_api.py

import fastapi
from typing import List
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from api import oauth2
from models import cars_models
from schema import cars_schema, users_schema
from databases.database import SessionLocal
from repository import cars_repo
import api.oauth2 as oauth2

router = fastapi.APIRouter(
    prefix="/cars",
    tags=['Cars']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/', response_model=List[cars_schema.ShowCar], status_code=status.HTTP_200_OK)
async def get_all_cars(db: Session = Depends(get_db)):
    cars = cars_repo.get_all(db)
    if not cars:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No cars currently available.")
    return cars


@router.get('/{id}', response_model=cars_schema.ShowCar, status_code=status.HTTP_200_OK)
async def get_car_by_id(id, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.id == id).first()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with the id {id} is not found.")
    return car


@router.get('/model/{model}', response_model=List[cars_schema.ShowCar], status_code=status.HTTP_200_OK)
async def get_car_by_model(model, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.model == model).all()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{model} does not exists or there are currently none available.")
    return car


@router.get('/make/{make}', response_model=List[cars_schema.ShowCar], status_code=status.HTTP_200_OK)
async def get_car_by_make(make, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.make == make).all()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{make} does not exists or there are currently none available.")
    return car


@router.get('/yom/{year_of_manufacture}', response_model=List[cars_schema.ShowCar], status_code=status.HTTP_200_OK)
async def get_car_by_year_of_manufacture(year_of_manufacture, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.year_of_manufacture == year_of_manufacture).all()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No cars manufactured in {year_of_manufacture} currently available.")
    return car


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_car(id, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.id == id)
    if not car.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Car with id {id} not found.")
    car.delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_car(id, request: cars_schema.Car, db: Session = Depends(get_db)):
    car = db.query(cars_models.Car).filter(cars_models.Car.id == id)
    if not car.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Car with id {id} not found.")
    car.update(request)
    db.commit()
    return 'updated'


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_car(request: cars_schema.ShowCar, db: Session = Depends(get_db)):
    new_car = cars_models.Car(
        make=request.make,
        model=request.model,
        year_of_manufacture=request.year_of_manufacture,
        miles=request.miles,
        condition_value=request.condition_value,
        color=request.color,
        price=request.price,
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car
