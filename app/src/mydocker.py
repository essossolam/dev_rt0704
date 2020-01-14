#!/usr/bin/python3
import docker
import os

client =  docker.from_env()

def run_container(image):
    client.containers.run(image,detach=True)

def containers_list():
    print (client.containers.list())

def build_docker_image():
    stream = os.popen('docker build -t worker_image:1.0 /home/jordy/dev_rt0704/app/.')
    output = stream.read()
    print (output)

build_docker_image()
run_container('worker_image:1.0')
containers_list()