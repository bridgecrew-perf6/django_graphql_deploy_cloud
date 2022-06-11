# Dockerfile for Django Applications
# Pull official base image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install OS dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

# Install python librairies 
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

# Set work directory
WORKDIR /app
ADD bookstore /app/

# RUN
COPY start.sh /app/
RUN chmod +x start.sh

ENTRYPOINT ["/app/start.sh" ]