FROM python:2.7-alpine 

RUN apk update && \
    apk add g++ && \
    apk add gmp

ADD pycrypto-2.6.1.tar.gz /home/src
WORKDIR /home/src/pycrypto-2.6.1
RUN python setup.py install

WORKDIR /
ADD hello.py /


