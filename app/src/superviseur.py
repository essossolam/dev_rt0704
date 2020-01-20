#!/usr/bin/python3
import pika
import json
import sys


def connection():
    return pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

def read_logs_queue(name):
    channel = connection().channel()
    channel.queue_declare(queue=name)
    channel.basic_consume(
    queue=name, on_message_callback=callback, auto_ack=True)
    print(' [*] Supervisions opérations de l architecture . Pour sortir cmd CTRL+C')
    channel.start_consuming()

read_logs_queue('logs')