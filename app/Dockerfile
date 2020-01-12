FROM debian:jessie
RUN apt-get update && apt-get install -y python3-pip python3-dev && cd /usr/local/bin && ln -s /usr/bin/python3 python && apt-get install git -y && pip3 install --upgrade pip 
RUN mkdir code_to_execute
COPY src/worker_code /code_to_execute

CMD python3 /code_to_execute/worker_client.py
