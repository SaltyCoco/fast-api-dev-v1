# models/cars_schema.py

from pydantic import BaseModel
from .users_schema import ShowUser


# Seems like UID is automatically assigned
class Car(BaseModel):
    make: str
    model: str
    year_of_manufacture: int
    miles: int
    condition_value: int
    color: str
    price: float


class ShowCar(BaseModel):
    make: str
    model: str
    year_of_manufacture: int
    miles: int
    condition_value: int
    color: str
    price: float

    class Config:
        orm_mode = True
