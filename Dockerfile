FROM python:3.7.6-buster
MAINTAINER Lukasz Admin

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN useradd user
USER user
