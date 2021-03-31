'''TODO:
    1. Look into pydantic.<models>
    2. Add delete
    3. Azure Deployment
    4. Connect to databases
    5. Find out what template generator the framework uses and fix the landing page.
'''

from fastapi import FastAPI

# from databases import database
from views import home
from api import cars_api
from schema import cars_schema
from databases.database import engine


api = FastAPI()

cars_schema.Base.metadata.create_all(engine)

def configure():
    api.include_router(home.router)
    api.include_router(cars_api.router)

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
