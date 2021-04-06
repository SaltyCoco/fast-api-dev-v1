# main.py

from fastapi import FastAPI

# from databases import database
from views import home
from api import cars_api, users_api
from models import cars_models, users_models
from api import authentication
from databases.database import engine

api = FastAPI()

cars_models.Base.metadata.create_all(engine)
users_models.Base.metadata.create_all(engine)


def configure():
    api.include_router(authentication.router)
    api.include_router(home.router)
    api.include_router(cars_api.router)
    api.include_router(users_api.router)


# These methods need to be created but I am not sure they even need to be there.
# @api.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @api.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


configure()

# if __name__ == '__main__':
#     uvicorn.run(api)
