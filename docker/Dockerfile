FROM debian:stretch
LABEL maintainer="benfonty@gmail.com"

RUN apt-get update && \
	apt-get install -y python && \
	apt-get install -y python-pip

RUN pip install Flask Flask-RESTful pymongo

COPY delivery/server.py /usr/local/server.py

CMD python /usr/local/server.py 
