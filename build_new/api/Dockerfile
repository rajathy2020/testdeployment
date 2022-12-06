FROM python:3.7

MAINTAINER rushi.soni@hy.co

USER root

RUN apt-get update --fix-missing

RUN apt-get -y install \
  python3-dev \
  netcat \
  vim \
  python-dev 

# Following needed for PDF layout parser
RUN pip install  --upgrade pip setuptools

RUN pip install \
  fastapi==0.60.1 \
  uvicorn 

WORKDIR /backend
