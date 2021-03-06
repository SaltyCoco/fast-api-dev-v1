## Application is running on Azure Container Service
- Using single container, for the [site](https://wa-fastapidev.azurewebsites.net/)
## sqlalchemy
- Notes for [SqlAlchemy](https://www.sqlalchemy.org)
- In the main.py there are two functiomns that open and close the connection to the db.
- You have to manually create the table migrations.
- When using SQLite you need to have the following but it is __NOT__ needed for postgres.
```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
```
## MSSQL
- This requires a lot of extra steps to get running on MAC and Ubuntu.  The steps are outlined [here](https://stackoverflow.com/questions/44527452/cant-open-lib-odbc-driver-13-for-sql-server-sym-linking-issue)
- For Mac this should work:
```shell script
# Step1: install unixodbc 
brew install unixodbc
# Step2: install Microsoft ODBC Driver for SQL Server on MacOS
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install msodbcsql mssql-tools
```
- For the docker image you will likely need to add:
```dockerfile
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17
RUN apt-get -y install unixodbc-dev
```
## pydantic
- [url](https://pydantic-docs.helpmanual.io)
- Has a built in ORM
## Run API
```shell script
uvicorn main:api --reload
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
1. Left click on template directory
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
## Main Difference Between models and Schema
- Models hold info for CRUD ops
- Schema holds info for SQLAlchmey