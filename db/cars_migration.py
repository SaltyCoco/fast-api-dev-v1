# db/cars_migration.py
import sqlalchemy

DATABASE_URL = "postgres://postgres:postgres@localhost:5432/postgres"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

cars = sqlalchemy.Table(
    "cars",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("make", sqlalchemy.String, foreign_key=True),
    sqlalchemy.Column("model", sqlalchemy.string),
    sqlalchemy.Column("year_of_manufacture", sqlalchemy.boolean),
    sqlalchemy.Column("miles", sqlalchemy.int),
    sqlalchemy.Column("condition_value", sqlalchemy.int),
    sqlalchemy.Column("color", sqlalchemy.string),
    sqlalchemy.Column("is_ready", sqlalchemy.boolean),
    sqlalchemy.Column("price", sqlalchemy.float),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
