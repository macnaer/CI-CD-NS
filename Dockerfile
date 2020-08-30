FROM python:latest

MAINTAINER macnaer

WORKDIR /home/dfo
COPY . /home/dfo

RUN cd /home/dfo && pip install -r requrements.txt

ENTRYPOINT ["start.py"]