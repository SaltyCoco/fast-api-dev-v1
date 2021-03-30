# models/cars.py
from pydantic import BaseModel


# Seems like UID is automatically assigned
class Car(BaseModel):
    make: str
    model: str
    year_of_manufacture: int
    miles: int
    condition_value: int
    color: str
    is_ready: bool
    price: float
