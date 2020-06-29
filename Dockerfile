FROM python:3.8-alpine

MAINTAINER Tiago Peres

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "run.py"]