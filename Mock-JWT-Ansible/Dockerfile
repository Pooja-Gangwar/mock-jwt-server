# Deriving the latest base image
FROM python:latest

LABEL Maintainer="Pooja Gangwar"

RUN python3 -m venv .env

RUN pip install -U pip
RUN pip install pyjwt[crypto]
RUN pip install pipenv
RUN pipenv install pyjwt
RUN pipenv install cryptography


WORKDIR /usr/app/src

# COPY jwt-generator.py jwt-velidator.py ./
COPY . .


RUN openssl req -x509 -nodes -newkey rsa:2048 -keyout private_key.pem -out public_key.pem -subj "/CN=jwt-tutorial"

CMD [ "python3", "./jwt-generator.py"]
