# Comment-system

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

#### О проекте
Comment-system - микросервис, в котором можно создавать статьи, комментировать
их,а также отвечать на комментарии

#### Стек реализации:
* Язык: Python 3.9
* Web framework: Django 3.2.12 & DRF 3.13.1
* Database: PostgreSQL

#### Доступные эндпоинты:

```
/article/
```
Метод запроса: POST

API создает статью

Запрос должен принимать:
- text - текст статьи

```
/article/<id статьи>/
```
Метод запроса: GET

Апи выдает статью с id указанным в запросе и
вложенные комментарии, ограниченные третьим уровнем вложенности

```
/article/<id статьи>/comment/
```
Метод запроса: POST

API создает комментарий к указанной в запросе статье

Запрос должен принимать:
- text - текст комментария

```
/article/<id статьи>/comment/<id комментария>/
```
Метод запроса: POST

API создает комментарий к указанному в запросе комментарию

Запрос должен принимать:
- text - текст комментария

```
/comments/
```
Метод запроса: GET

API получает комментарий 3го уровня вложенности и комментарии к нему

Запрос должен принимать:
- article - id статьи, комментарии которой мы хотим получить

```
/swagger/
/redoc/
```
Метод запроса: GET

Эндпоинты для получения информации по эндпоинтам API

#### Что бы протестировать приложение необходимо:

* клонировать репозиторий

```
git clone https://github.com/A1exit/comment-system.git
```

* создать файл .env и вставить в него переменные и добавить к ним необходимые значения


```
SECRET_KEY= (можно использовать дефолтный, он указан в настройках)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
* перейти в директорию с файлом docker-compose.yaml
* ввести в терминале: 
```
docker-compose up -d --build
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser - 
команда для создания суперпользователя для работы с админкой
```

#### Aвтор:

Алексей Останин
