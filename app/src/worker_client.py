import requests
import json
import os


APIENDPOINT = "http://127.0.0.1:5000"

#GET messages from a queue
r = requests.get("{}/rabbit/TODO".format(APIENDPOINT))
print("statut:{}".format(r.status_code))
data = json.loads(r.text)
stream1 = os.popen('git clone {}'.format(data['code']))
stream1.read()
stream2 = os.popen('python /rt0704/ndame.py 4')
output = stream2.read()
print (output)

