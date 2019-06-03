FROM python:3.7-alpine

WORKDIR .
ENV AWS_ACCESS_KEY_ID id
ENV AWS_SECRET_ACCESS_KEY key
ENV AWS_DEFAULT_REGION us-west-2
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
