# AirOffice

This is an app under development aimed at customer management. Through a Ticket organizer and a Booking Organizer!

Application based on the Python Django Framework and related Django-REST API library for the back-end.
Frontend developed on reactJS basis.

Different back-end and front-end libraries are used for development.


### Python Version

``
Python 3.10
``

## Dev Support

### Create dev data for sb
*Start in folder of db_init.py*
```
python db_init.py
```

## Dev Support
 - [Docker](https://www.docker.com/)
 
## BackEnd Lib

 - [Django](https://www.djangoproject.com/)
 - [Rest Framework](https://www.django-rest-framework.org/)

 *Future Implementation*
 - [Celery](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)


## [FrontEnd Lib](https://fireart.studio/blog/9-react-best-practices-to-improve-your-react-code/)

  - [HeadlessuI](https://headlessui.com/)
  - [Heroicons](https://heroicons.com/)
  - [Tailwindcss](https://tailwindcss.com/)
  - [Sass](https://sass-lang.com/)
  - [axios-http](https://axios-http.com/docs/intro)
  - [vueuse](https://vueuse.org/)
  - [google icon](https://fonts.google.com/icons)

# Commands
### [Venv](https://docs.python.org/3/library/venv.html) Python library management environment

Init VirtualEnviroment
```
python -m venv venv
```
Start venv
```
./venv/Scripts/activate
```
Stop venv
```
deactivate
```

### Docker
install docker from [Docker](https://www.docker.com/)

Build Docker
*In dir ./merger/*
```
docker compose -f docker/docker-compose.yaml build
```
Launch Docker container
*In dir ``./merger/``*
```
docker compose -f docker/docker-compose.yaml up -d
```
Prune Docker
*In dir ``./merger/``*
in case of delete container
```
docker compose -f docker/docker-compose.yaml up -d
```

### [Django] Web Framework Python lang.

Db Migrations init
```
python manage.py makemigrations
```
Db Migrate 
```
python manage.py migrate
```
Start Server
```
python manage.py runserver
```
### [VueJs] FrontEnd JS Framework

#### *In local direcory (./frontend)*

Install Library
```
npm install 
```
Start Dev server 
```
npm run serve 
```







