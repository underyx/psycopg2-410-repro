FROM python:3-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN apk add --no-cache --virtual=.run-deps libpq && \
    apk add --no-cache --virtual=.build-deps build-base postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps
COPY . /app

CMD [ "python", "/app/repro.py" ]
