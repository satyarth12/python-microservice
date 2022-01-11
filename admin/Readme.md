## Admin site in the microservice application
 - This is the admin part of the microvervice application, built in django.
 - The admin app's APIs will allow the admin/superuser to access and edit the dashboard pannel of the application.

## Activating pipenv, Installing Dependencies
```
pipenv shell
cd admin
pipenv install -r requirements.txt
```

## Configure and Running Admin Project
1. Running server Locally on PC's default cmd
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
2. Running server on Docker & Accessing Docker shell
```
docker-compose up
```
- This command, given below, will help the developer to access the docker-shell of the admin image, to perform django related commands on docker cmd.
```
docker-compose exec backend sh
```
 
