# Django + GraphQL + Docker

This project is a simple Django application based on GraphQL and a bookstore usecase. GraphQL is a query language for APIs that gives clients the ability to ask exactly what they need from APIs.

## Project Structure

The project is split into two parts:

1. __Backend GraphLQ API__: Django web application.

2. __Dockerize the Django app__: Docker, Python, and Gunicorn web server.

### Local Environment Instructions

#### Installation
```
$ pip install Django
$ pip install graphene-django
```

#### Set up the Django project
Clone the repository, and navigate to the downloaded folder. 
	```
	git clone https://github.com/nalbert9/django_graphql_deploy_cloud.git
	```
#### Run the project on local
```
$ cd bookstore
$ python manage.py runserver
```
