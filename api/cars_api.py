# api/cars_api.py
from typing import Optional
import fastapi

from models.cars import Car

router = fastapi.APIRouter()


@router.get("/api/cars", response_model=Car)
def car_make_search(car: Car = fastapi.Depends()):
    return car

##############################################################################################
# Cars API Cals
##############################################################################################
@router.get("/api/cars/{car_id}")
def read_car(car_id: int, q: Optional[str] = None):
    return {"car_id": car_id, "q": q}


@router.put("/api/cars/{car_id}")
def update_car(car_id: int, car: Car):
    return {
        "car_id": car_id,
        "car_make": car.make,
        "car_model": car.model,
        "car_year_of_manufacture": car.year_of_manufacture,
        "car_miles": car.miles,
        "car_condition_value": car.condition_value,
        "car_color": car.color,
        "car_price": car.price
    }

