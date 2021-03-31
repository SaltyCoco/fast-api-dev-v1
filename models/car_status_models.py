# models/cars_status.py
from pydantic import BaseModel


class CarStatus(BaseModel):
    id: int
    car_id: int
    is_ready: bool
    is_pending_sale: bool
    is_sold: bool
    is_unavailable: bool
    is_in_transit: bool
    is_unknown: bool