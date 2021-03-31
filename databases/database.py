# databases/database.py
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = 'postgresql+psycopg2://postgres:Bryan1940?@10.50.5.7:5432/db_mipc'
# DATABASE_URL = "postgres://postgres:postgres@localhost:5432/postgres"
# DATABASE_URL = "sqlite:///./db_fastapi_dev.db"

# metadata = sqlalchemy.MetaData()
#
# cars = sqlalchemy.Table(
#     "cars",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
#     sqlalchemy.Column("make", sqlalchemy.String)
#     sqlalchemy.Column("model", sqlalchemy.String)
#     sqlalchemy.Column("year_of_manufacture", sqlalchemy.SmallInteger)
#     sqlalchemy.Column("miles", sqlalchemy.Integer)
#     sqlalchemy.Column("condition_value", sqlalchemy.SmallInteger)
#     sqlalchemy.Column("color", sqlalchemy.String)
#     sqlalchemy.Column("price", sqlalchemy.Float)
# )

# engine = sqlalchemy.create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./db_fastapi_dev.db"
# DATABASE_URL = "postgres://postgres:postgres@localhost:5432/postgres"
# DATABASE_URL = 'postgresql+psycopg2://postgres:Bryan1940?@10.50.5.7:5432/db_mipc'

# connect_args={"check_same_thread": False} is needed for SQLite ONLY
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
# engine = create_engine(
#     DATABASE_URL
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

