FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update
WORKDIR /app
RUN pip3 install pip-tools
COPY requirements.in /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /code