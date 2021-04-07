# databases/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
# import pyodbc
import os


dir = os.path.dirname(__file__)
cfg = ConfigParser()
cfg.read(os.path.join(dir, 'azure_envs.ini'))


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
FASTAPI_AZURE_USER = cfg.get('envs', 'FASTAPI_AZURE_USER')
FASTAPI_AZURE_PASSWORD = cfg.get('envs', 'FASTAPI_AZURE_PASSWORD')
FASTAPI_AZURE_HOST = cfg.get('envs', 'FASTAPI_AZURE_HOST')
FASTAPI_AZURE_DB = cfg.get('envs', 'FASTAPI_AZURE_DB')
# engine = create_engine(f'mssql+pyodbc://{user}:{password}@{host}/{db}?driver=ODBC+Driver+17+for+SQL+Server')


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
