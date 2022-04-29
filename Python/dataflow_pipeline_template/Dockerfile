#REPLACE VERSION WITH APPROPRIATE VALUE
FROM python:VERSION

ENV PIPENV_VENV_IN_PROJECT 1

WORKDIR /app

RUN apt-get update && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy

COPY . /app
RUN /app/.venv/bin/pip install .
