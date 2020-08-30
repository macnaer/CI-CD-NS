FROM python:latest

MAINTAINER macnaer

RUN apt update -y && apt-get install -y awscli
RUN cd ~ && cd .aws/ && pwd && ls -l
COPY . /root/.aws
WORKDIR /home/dfo
COPY . /home/dfo
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "start.py" ]
