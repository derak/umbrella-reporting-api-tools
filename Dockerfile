FROM python:3.7-stretch

RUN pip install --upgrade pip

ADD requirements.txt /opt/

WORKDIR /opt
RUN pip install -r requirements.txt
