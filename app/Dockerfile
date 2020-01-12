FROM debian:jessie
RUN apt-get update && apt-get install -y python3-pip python3-dev && cd /usr/local/bin && ln -s /usr/bin/python3 python && apt-get install git -y && pip3 install --upgrade pip 
RUN mkdir code
COPY src/worker_code /code

CMD python3 /code/worker_client.py
