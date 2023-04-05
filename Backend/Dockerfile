FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1
RUN mkdir /app
WORKDIR /app
EXPOSE 8000

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . /app/
RUN python manage.py collectstatic --no-input