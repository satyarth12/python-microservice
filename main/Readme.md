## Main site in the microservice application
 - This is the main part of the microvervice application, built in Flask.
 - Normal users or non-admin/superusers can access the APIs of main app to deal with the products.

## Activating pipenv, Installing Dependencies
```
pipenv shell
cd main
pipenv install -r requirements.txt
```

## Configure and Running Admin Project
Running server on Docker & Accessing Docker shell
```
docker-compose up
```
- Commands listed below are for:
    - accessing the docker shell
    - Checking the commands available for 'db', flask's app name in manager.py file.
    - Initializing db connection with mysql
    - Create the migrations folder for the models in main.py 
    - Migrating/Upgrading the model's schema to mysql's table
```
docker-compose exec backend sh
python manager.py db --help
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```
 
