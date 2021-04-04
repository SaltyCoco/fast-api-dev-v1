# databases/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc
import os
import urllib

# DATABASE_URL = "sqlite:///./db_fastapi_dev.db"
# DATABASE_URL = "postgres://postgres:postgres@localhost:5432/postgres"
# params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
#                                  "SERVER=fastapi-dev.database.windows.net;"
#                                  "DATABASE=db_fastapi_dev;"
#                                  "UID=RyanDevAdmin;"
#                                  "PWD=" + SQLSERVER_PWD)
#
# engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
# connect_args={"check_same_thread": False} is needed for SQLite ONLY
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )

# Azure MSSQL engine
# engine = create_engine(
#     SQLSERVER_DATABASE
# )
# user = os.getenv('user')
user = "RyanAdminDev"
password = os.getenv('password')
# host = os.getenv('SERVER_ADDRESS')
host = "fastapi-dev.database.windows.net"
# db = os.getenv('DATABASE')
db = "db_fastapi_dev"
engine = create_engine(f'mssql+pyodbc://{user}:{password}@fastapi-dev.database.windows.net/{db}?driver=ODBC+Driver+17+for+SQL+Server')


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
