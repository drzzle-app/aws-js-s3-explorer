FROM python:latest

MAINTAINER Drizzzle Devs "devs@drizzzle.com"

COPY . .

CMD ["python", "-m", "http.server", "8001"]
