FROM python:3.4-alpine3.4
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache bash && apk add --no-cache curl && apk add --no-cache iproute2
RUN mkdir /dcms
WORKDIR /dcms
ADD requirements.txt /dcms/
RUN pip install -r requirements.txt
ADD . /dcms/