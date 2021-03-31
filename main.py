'''TODO:
    1. Look into pydantic.<models>
    2. Add delete
    3. Azure Deployment
    4. Connect to db
    5. Find out what template generator the framework uses and fix the landing page.
'''

import uvicorn
from fastapi import FastAPI

from views import home
from api import cars_api

api = FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(cars_api.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


configure()

if __name__ == '__main__':
    uvicorn.run(api)
