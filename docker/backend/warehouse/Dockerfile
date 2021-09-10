FROM python:latest

ENV \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # dockerize:
    DOCKERIZE_VERSION=v0.6.1

WORKDIR /pysetup

# Project initialization:
COPY ./backend/warehouse/requirements.txt .

RUN pip install -r requirements.txt

# Installing `dockerize` utility:
# https://github.com/jwilder/dockerize
RUN wget "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && tar -C /usr/local/bin -xzvf "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && rm "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz"

# This is a special case. We need to run this script as an entry point:
COPY ./docker/backend/warehouse/docker-entrypoint.sh ./docker/backend/warehouse/wait-for-command.sh ./docker/backend/warehouse/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

# This dir will become the mountpoint of development code:
WORKDIR /code

ENTRYPOINT ["/docker-entrypoint.sh"]