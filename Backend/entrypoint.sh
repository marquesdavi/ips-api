#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrations
echo "Running migrations"
python manage.py makemigrations
python manage.py migrate

# Start Gunicorn
exec gunicorn setup.wsgi:application --bind 0.0.0.0:8000
