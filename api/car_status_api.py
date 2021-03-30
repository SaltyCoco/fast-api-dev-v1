# api/cars_api.py
from typing import Optional
import fastapi

from models.car_status import CarStatus

router = fastapi.APIRouter()

# models/cars.py
from pydantic import BaseModel


