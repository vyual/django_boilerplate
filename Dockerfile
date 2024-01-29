FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN apt-get update && apt-get install -y gunicorn3
