FROM python:3.11-buster

RUN pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml pyproject.toml 
COPY src src
RUN touch README.md

RUN poetry install --without dev

ENTRYPOINT [ "poetry", "run", "python", "-m", "src.app"]