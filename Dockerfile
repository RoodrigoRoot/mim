FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /mim

WORKDIR /mim

COPY requirements.txt /mim/

RUN pip install -r requirements.txt

COPY . /mim/