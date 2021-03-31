# api/cars_api.py
import fastapi

# from models.cars import Car
from databases.database import SessionLocal

router = fastapi.APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.get("/cars/", response_model=List[Car])
# async def get_all_cars():
#     query = Car.select()
#     return await SessionLocal.fetch_all(query)


# @router.get("/api/cars/{car_id}")
# async def read_car(car_id: int, q: Optional[str] = None):
#     return {"car_id": car_id, "q": q}
#
#
# @router.put("/api/cars/{car_id}")
# async def update_car(car_id: int, car: Car):
#     return {
#         "car_id": car_id,
#         "car_make": car.make,
#         "car_model": car.model,
#         "car_year_of_manufacture": car.year_of_manufacture,
#         "car_miles": car.miles,
#         "car_condition_value": car.condition_value,
#         "car_color": car.color,
#         "car_price": car.price
#     }
#
#
# @router.get("/api/cars", response_model=Car)
# async def car_make_search(car: Car = fastapi.Depends()):
#     return {
#         "car_make": car.make,
#         "car_model": car.model,
#         "car_year_of_manufacture": car.year_of_manufacture,
#         "car_miles": car.miles,
#         "car_condition_value": car.condition_value,
#         "car_color": car.color,
#         "car_price": car.price
#     }
