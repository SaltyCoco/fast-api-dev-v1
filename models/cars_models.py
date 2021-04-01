# schema/cars_schema.py

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, SmallInteger
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.ext.declarative import declarative_base

from databases.database import Base

# Seems like UID is automatically assigned
class Car(Base):
    __tablename__ = 'cars'

    # id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    year_of_manufacture = Column(SmallInteger)
    miles = Column(Integer)
    condition_value = Column(Integer)
    color = Column(String)
    price = Column(Float)


