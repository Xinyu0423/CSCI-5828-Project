FROM python:3.9-alpine

LABEL maintainer="kevgao@live.com"

WORKDIR /api
COPY Pipfile Pipfile.lock ./
COPY app app
COPY migrations migrations

RUN apk --no-cache add build-base && \
    apk --no-cache add postgresql-dev && \
    pip install pipenv && \
    pipenv install $(test "$ENVIRONMENT" == production || echo "--dev") --deploy --system --ignore-pipfile

EXPOSE 5000 

CMD gunicorn --bind 0.0.0.0:$PORT 'app:create_app()'