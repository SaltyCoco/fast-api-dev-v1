# models/cars_models.py

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, SmallInteger, Boolean
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.ext.declarative import declarative_base

from databases.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

