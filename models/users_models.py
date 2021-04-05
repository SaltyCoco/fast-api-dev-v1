# models/cars_models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from databases.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    cars = relationship('Car', back_populates="seller")
