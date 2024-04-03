FROM python:3.11.2-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
