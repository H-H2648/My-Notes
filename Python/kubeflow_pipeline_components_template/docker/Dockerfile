# substitute appropriate version for APPROPRIATE_VERSION below
FROM python:APPROPRIATE_VERSION

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip install pipenv

COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock
RUN pipenv install --deploy --system

COPY ./src ./src
