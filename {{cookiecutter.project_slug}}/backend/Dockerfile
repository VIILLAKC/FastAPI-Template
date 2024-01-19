FROM python:3.12.0

WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .