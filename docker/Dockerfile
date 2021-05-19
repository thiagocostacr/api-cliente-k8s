FROM python:3.8-slim-buster

MAINTAINER "Thiago Costa Cirqueira <thiago.costa.cr@gmail.com>"

COPY ../requirements.txt /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=app.py
ENV JSON_SORT_KEYS=False

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
RUN pip3 install -r requirements.txt

COPY ../ .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
