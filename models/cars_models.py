# schema/cars_schema.py

from sqlalchemy import Column, Integer, String, Float, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base


# Seems like UID is automatically assigned
class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    year_of_manufacture = Column(SmallInteger)
    miles = Column(Integer)
    condition_value = Column(Integer)
    color = Column(String)
    price = Column(Float)