# Django + GraphQL + Docker

This project is a simple [Django](https://www.djangoproject.com/) application based on GraphQL. [GraphQL](https://graphql.org/) is a query language for APIs that gives clients the ability to ask exactly what they need from APIs.

## Project Structure

The project is split into two parts:

1. __Backend GraphLQ API__: Django web application (bookstore usecase).

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

#### Run the project with Docker
[Docker](https://docs.docker.com/) gives us the ability to run our applications within a controlled environment, known as a container, built according to the instructions we define. We can manage docker apps with [Docker compose](https://docs.docker.com/compose/), [Kubernetes Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)..etc.

```
$ docker build -t bookstoreapi:1.1 .
$ docker run bookstoreapi:1.1
```
