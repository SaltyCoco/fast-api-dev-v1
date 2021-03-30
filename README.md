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
## Get Auto Complete for Jinja2 Templates
1. Left click on tmeplate direcotry
2. Go to "Mark Directory As" and select template
3. It will likely ask you what language you want, select yes.
4. The pycharm options will pop up, go to "languages & frameworks"
5. Select "Template Language"
6. Click on "HTML" in the template file types
7. In the "Template language" drop down select Jinja2
8. Click Apply then OK
## Views
- You do not want to have the html routes in the API docs so use the following in the decorator:
```python
@router.get("/", include_in_schema=False)
```