# api/cars_api.py
from typing import Optional
import fastapi

from models.car_status_models import CarStatus

router = fastapi.APIRouter()

# models/cars_models.py
from pydantic import BaseModel


