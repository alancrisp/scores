FROM python:3.8-alpine

WORKDIR /app

RUN apk add build-base mariadb-dev

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
