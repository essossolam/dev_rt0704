import requests
import json
import os

APIENDPOINT = "http://172.17.0.1:5000"

# GET messages from a queue
hasTask = True
while hasTask:
    r = requests.get("{}/rabbit/TODO".format(APIENDPOINT))
    if (r.text != '0'):
        data = json.loads(r.text)
        stream1 = os.popen('git clone {}'.format(data['code']))
        stream1.read()
        stream2 = os.popen('git clone {}'.format(data['params']))
        stream2.read()
        with open('parameters.txt') as json_file:
            params = json.load(json_file)
            for p in params['task_param']:
            if (p['pid'] == data['pid'] and p['task_id'] == data['id']):
                stream3 = os.popen('python /code/ndame.py {}'.format(params['input']))
                output = stream3.read()
                print(output)
    else:
        hasTask = False
