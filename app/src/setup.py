import requests
import json
import os

#Ce fichier permet d'initialiser le conteneur rabbitmq avec
#les files "TODO" et "DONE"


APIENDPOINT = "http://172.17.0.1:5000"

# #POST create new queue
# payload= {}
# queue = ['TODO', 'DONE']
# for q in queue:
#     payload['queue_name'] = q
#     mydata = {"data": json.dumps(payload)}
#     r = requests.post("{}/rabbit".format(APIENDPOINT), data=mydata)
#     print("statut:{}".format(r.status_code))
#     print(r.text)

payload= {}
payload['queue_name'] = 'logs'
mydata = {"data": json.dumps(payload)}
r = requests.post("{}/rabbit".format(APIENDPOINT), data=mydata)
print("statut:{}".format(r.status_code))
print(r.text)

payload= {}
payload['message'] = 'tache reçu'
mydata = {"data": json.dumps(payload)}
r = requests.post("{}/rabbit/logs/{}".format(APIENDPOINT,'logs'), data=mydata)
print("statut:{}".format(r.status_code))
print(r.text)