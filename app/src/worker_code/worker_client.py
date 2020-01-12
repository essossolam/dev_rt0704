import requests
import json
import os

APIENDPOINT = "http://172.17.0.1:5000"

#GET messages from a queue
hasTask = True
while hasTask:
    r = requests.get("{}/rabbit/TODO".format(APIENDPOINT))
    if (r.text != '0'):
        data = json.loads(r.text)
        stream1 = os.popen('git clone {}'.format(data['code']))
        stream1.read()
        stream2 = os.popen('python /rt0704/ndame.py 8')
        output = stream2.read()
        print (output)
    else:
        hasTask = False
