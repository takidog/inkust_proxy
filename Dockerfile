FROM python:3.7-alpine
# Create app directory
RUN mkdir -p /usr/src/inkust_proxy
WORKDIR /usr/src/inkust_proxy

COPY . /usr/src/inkust_proxy

RUN pip3 install -r ./requirements.txt


# WORKDIR .

CMD ["gunicorn","-c","gunicorn_config.py","web-server:app"]