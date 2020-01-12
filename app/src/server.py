#!/usr/bin/python3

from flask import Flask, request
from producer import create_queue, write_in_queue, read_queue
import pika
import json

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world !"

@app.route('/rabbit', methods=['POST'])
def rabbit():
    data = json.loads(request.form['data'])
    
    create_queue(data['queue_name'])
    r = {}
    r['status'] = "Ok"
    r['message'] = "queue successfully created"
    reponse = {'data': json.dumps(r)}
    return reponse

@app.route('/rabbit/<nom_file>', methods=['POST'])
def depot_message(nom_file):
    data = json.loads(request.form['data'])
    write_in_queue(nom_file, data['task'])

    return "Successfully writed!"

@app.route('/rabbit/<nom_file>', methods=['GET'])
def read_message(nom_file):
    r = read_queue(nom_file)
    response =  r
    return response
    

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000,debug=True)