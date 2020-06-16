FROM python:3.7.7-alpine

RUN pip install pipenv

RUN apk --update add \
	git \
	bash \
	openssh

RUN mkdir -p /project && cd /project
COPY . /project/

WORKDIR /project/
RUN pipenv install --dev -e .


	
