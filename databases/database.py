# databases/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc

# DATABASE_URL = "sqlite:///./db_fastapi_dev.db"
# DATABASE_URL = "postgres://postgres:postgres@localhost:5432/postgres"
SQLSERVER_DATABASE = "mssql+pyodbc://RyanDevAdmin:RSC211982!Bryan1940!@fastapi-dev.database.windows.net/db_fastapi_dev?driver=ODBC+Driver+17+for+SQL+Server"

# connect_args={"check_same_thread": False} is needed for SQLite ONLY
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )

# Azure MSSQL engine
engine = create_engine(
    SQLSERVER_DATABASE
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

