# Alguns tutoriais:

https://youtu.be/FnGxwmtUK0c?list=PLMEVlrVfhrHvrEkfdm85z5_YSNOYKYW2g



# Comandos básicos:



# Dockerfile's

## Python

```docker
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ['sh','-c','python manage.py migrate && python manage.py runserver 0.0.0.0:8000]

```