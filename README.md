# 2024-04-13-backend
technical test


## To run in local
### docker-compose
You need to have installed docker, once in the project folder,
run:
    docker-compose-up
now you got the container fot the db in localhost port 5432
yo may config pg-admin(in the container) to admin the db and run the structure 
described bellow

### .env to develop
### Here the dotenv required to the project, the values are valid just for develop env

POSTGRES_HOST=localhost
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
DB_NAME=postgres
PG_MAIL=admin@admin.com
PG_PASSWORD=admin
CORS_HOST=*

### Install dependencies

Just need to run:
    pip install -r requirements.txt

### Run project dev

Just need to run:
    uvicorn main:app --reload

### Run project prod

Just need to run:
    uvicorn main:app --host 0.0.0.0



