# repository/cars_repo.py

from sqlalchemy.orm import Session
from models import cars_models
from fastapi import Depends, status, Response, HTTPException


def get_all(db: Session):
    cars = db.query(cars_models.Car).all()
    if not cars:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No cars currently available.")
    return cars


def get_one(id: int, db: Session):
    car = db.query(cars_models.Car).filter(cars_models.Car.id == id).first()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with the id {id} is not found.")
    return car

