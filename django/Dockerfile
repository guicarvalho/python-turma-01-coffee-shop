FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
COPY ./ .

RUN apk --update --upgrade add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev  && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

CMD python coffee_shop/manage.py runserver 0.0.0.0:8000

