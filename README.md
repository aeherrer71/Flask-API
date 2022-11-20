# Python-API-Project
- This a RESTful API project with full CRUD. This project was created with Python, Flask, Peewee, PostgreSQL.

## Running the Program

- In order to get this program started the user requires pipenv to be installed. 
- Run a virtual environment (pipenv shell)
- Install dependencies: Flask, Peewee, Psycopg2-binary
- Run python3 on the app.py file

## Endpoints

- GET & POST Requests: /employee  a get request to this endpoint returns all the staff at this company. A post request to this endpoint creates a new employee. 

- GET, PUT, & DELETE Requests: /employee/<id> a get request to this endpoint returns a single employee. A put request to this endpoint updates a single employee, and a Delete request to this endpoint removes the employee from the database. 
