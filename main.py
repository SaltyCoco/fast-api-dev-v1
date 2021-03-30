'''TODO:
    1. Look into pydantic.<models>
    2. Add delete
    3. Azure Deployment
    4. Connect to db
    5. Find out what template generator the framework uses and fix the landing page.
'''

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Uses classes as models like django
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

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

# Cannot use string html
@app.get("/")
def read_root():
    return {"""
        <html>
          <head>
            <title>Car API</title>
          </head>
          <body>
            <h1>Welcome to the Car API Info Page</h1>
            <h3>Authorization & Authentication</h3>
            <p>Please contact Padme Almedala for your api token.</p>
          </body>
        </html>
    """}

###############################################################################################
# Cars Items Cals - This was the prebuilt portion from the site
###############################################################################################
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

###############################################################################################
# Cars API Cals
###############################################################################################
@app.get("/cars/{car_id}")
def read_item(car_id: int, q: Optional[str] = None):
    return {"car_id": car_id, "q": q}

@app.put("/cars/{car_id}")
def update_item(car_id: int, car: Car):
    return {
        "car_id": car_id,
        "car_make": car.make,
        "car_model": car.model,
        "car_year_of_manufacture": car.year_of_manufacture,
        "car_miles": car.miles,
        "car_condition_value": car.condition_value,
        "car_color": car.color,
        "car_is_ready": car.is_ready,
        "car_price": car.price
    }
