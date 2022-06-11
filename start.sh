#!/bin/bash

# Run GraphQL server with gunicorn
gunicorn --workers 4 --chdir /app/bookstore bookstore.wsgi:application