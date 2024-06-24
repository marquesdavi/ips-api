FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . /app/
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

RUN python manage.py collectstatic --no-input

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
