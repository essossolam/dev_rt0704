#!/usr/bin/python3
import pika
import json
import sys

def connection():
    return pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

def create_queue(name):
    channel = connection().channel()
    channel.queue_declare(queue=name)
    connection().close()
   


def write_in_queue(name,message):
    channel = connection().channel()
    channel.basic_publish(
        exchange='', routing_key=name, body=json.dumps(message))



def read_queue(name):
    channel = connection().channel()
    method_frame, header_frame, body = channel.basic_get(name)
    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)
        return json.loads(body)
    else:
        return '0'



