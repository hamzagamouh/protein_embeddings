FROM python:3.7.13-slim-buster
WORKDIR /app

COPY . .

RUN cd /app

RUN pip install -r requirements.txt



