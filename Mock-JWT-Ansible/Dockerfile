# Deriving the latest base image
FROM python:latest

LABEL Maintainer="Pooja Gangwar"

# RUN python3 -m venv .env

RUN python3 -m venv .env && \
    pip install -U pip && \
    pip install pyjwt[crypto] && \
    pip install pipenv && \
    pipenv install pyjwt && \
    pipenv install cryptography

WORKDIR /usr/app/src

# RUN chmod +x keys.sh
# RUN ./keys.sh
CMD [ "python3", "./jwt-generator.py"]
