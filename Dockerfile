
FROM python:3.9.16-slim

LABEL maintainer="Salman Raza <razasalman2019@gmail.com>"

RUN apt-get update; apt-get install curl -y

# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry POETRY_VERSION=1.2.0 python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

ARG APP_DIR=/app
ARG LOCAL_DIR=.

# Create app user and group
ARG APP_USR=appusr
ARG APP_GRP=appgrp

RUN groupadd -r $APP_GRP
RUN useradd -r -m $APP_USR
RUN usermod -a -G $APP_GRP $APP_USR

# Create app directory
WORKDIR $APP_DIR
RUN chown $APP_USR:$APP_GRP $APP_DIR

# Install dependencies
COPY --chown=$APP_USR:$APP_GRP ./$LOCAL_DIR/pyproject.toml ./$LOCAL_DIR/poetry.lock* ./
RUN poetry install --no-root --no-dev

# Install API application into the container
COPY --chown=$APP_USR:$APP_GRP ./$LOCAL_DIR/app ./app
COPY --chown=$APP_USR:$APP_GRP ./$LOCAL_DIR/.env ./.env
COPY --chown=$APP_USR:$APP_GRP ./$LOCAL_DIR/start_app.py ./start_app.py

# Become appusr
USER $APP_USR
