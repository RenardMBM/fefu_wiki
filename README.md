# fefu_wiki

## Requirements
___
### Backend
* Docker
* Python 3

## Run
___
### Backend
1) Get up database
    ``` shell
    docker-compose -f .docker\docker-compose.yml up database
    ```
2) Set environment variables
    ```
   DATABASE_NAME = dbName
   POSTGRES_USER = dbUser
   POSTGRES_PASSWORD = dbPassword
   ```
3) Run backend server
    ``` shell
    python manage.py runserver localhost:8000
    ```