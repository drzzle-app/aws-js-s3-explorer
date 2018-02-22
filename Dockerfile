FROM python:latest

MAINTAINER Drizzzle Devs "devs@drizzzle.com"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "./run.py"]

EXPOSE 8001
