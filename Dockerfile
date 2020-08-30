FROM python:latest

MAINTAINER macnaer

WORKDIR /home/dfo
COPY . /home/dfo
RUN pip install -r requirements.txt
