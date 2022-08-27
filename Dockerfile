FROM python:3.10.1-buster
MAINTAINER Lukasz Admin

RUN apt-get update

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN useradd -ms /bin/bash admin

COPY ./app/ /usr/src/app

RUN chown -R admin:admin /usr/src/app
RUN chmod 755 /usr/src/app
USER admin

EXPOSE 80

CMD ["gunicorn", "portal.wsgi", "--bind=0.0.0.0:80"]