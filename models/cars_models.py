# models/cars_models.py
from pydantic import BaseModel


# Seems like UID is automatically assigned
class Car(BaseModel):
    id: int
    make: str
    model: str
    year_of_manufacture: int
    miles: int
    condition_value: int
    color: str
    price: float

    class Config:
        orm_mode = True

class CarCreate(Car):
    pass