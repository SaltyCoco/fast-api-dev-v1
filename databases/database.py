# databases/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc
import os
import urllib

DATABASE_URL = "sqlite:///./db_fastapi_dev.db"
# DATABASE_URL = "postgres://postgres:postgres@localhost:5432/postgres"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# DATABASE_URL = "postgres://postgres:postgres@localhost:5432/postgres"
# engine = create_engine(
#     DATABASE_URL}
# )

# Azure MSSQL engine
# engine = create_engine(
#     SQLSERVER_DATABASE
# )

# Azure MSSQL engine
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('SERVER_ADDRESS')
db = os.getenv('DATABASE')
# engine = create_engine(f'mssql+pyodbc://{user}:{password}@{host}/{db}?driver=ODBC+Driver+17+for+SQL+Server')


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
