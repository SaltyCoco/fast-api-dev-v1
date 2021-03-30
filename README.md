## pydantic
- [url](https://pydantic-docs.helpmanual.io)
- Has a built in ORM
## Run API
```shell script
uvicorn main:app --reload
```
- run with Docker
```shell script
docker run -p 8000:8000 fast-api-test:latest
```
## starlette
- Did not work with version 14.2 but did with 13.8
## Check running API
- go to [url](http://127.0.0.1:8000/items/5?q=somequery)
- Swagger [url](http://127.0.0.1:8000/docs)
- ReDoc [url](http://127.0.0.1:8000/redoc)
## Check for App running on port and kill
```shell script
lsof -i tcp:8000 
kill -9 <PID of app>
```