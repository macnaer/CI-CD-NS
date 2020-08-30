FROM python:latest

MAINTAINER macnaer

WORKDIR /home/dfo
COPY . /home/dfo
RUN pwd
RUN cd /home/dfo && pwd
RUN pip install -r requrements.txt

ENTRYPOINT ["start.py"]