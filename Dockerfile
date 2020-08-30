FROM python:latest

MAINTAINER macnaer

RUN apt update -y && apt-get install -y awscli
RUN pwd && ls -la
RUN cd /root && pwd && ls -la
COPY /root/.aws/* /root/.aws
WORKDIR /home/dfo
COPY . /home/dfo
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "start.py" ]
