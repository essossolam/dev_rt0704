#!/usr/bin/python3
#Code du commanditaire 
import requests
import json
import os
from mygit import git_add_file, git_commit, git_push, git_init, git_pull

APIENDPOINT = "http://127.0.0.1:5000"
basepath = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(os.path.dirname(basepath))

#création des tâches sous format JSON
task = {
    "pid":1,
    "id":1,
    "code":"https://github.com/essossolam/dev_rt0704/app/src/code",
    "params":"https://github.com/essossolam/rt0704"
}

#Envoie des paramètres sur git
git_add_file("{}/param/paramaters.txt".format(basepath), parentDir)
git_commit(parentDir,"The damen problem parameters")
git_push(parentDir)
#Envoie du code sur git
git_add_file("{}/code/ndame.py".format(basepath), parentDir)
git_commit(parentDir,"The damen problem code")
git_push(parentDir)
#git_init()
#POST create new queue
# payload= {}
# queue1 = 'TODO'
# queue2 = 'DONE'
# payload['queue_name'] = queue1
# mydata = {"data": json.dumps(payload)}
# r = requests.post("{}/rabbit".format(APIENDPOINT), data=mydata)
# print("statut:{}".format(r.status_code))
# print(r.text)

#POST insert new message in queue
# payload= {}
# queue1 = 'TODO'
# queue2 = 'DONE'
# payload['task'] = task
# mydata = {"data": json.dumps(payload)}
# r = requests.post("{}/rabbit/{}".format(APIENDPOINT,queue1), data=mydata)
# print("statut:{}".format(r.status_code))
# print(r.text)


# #GET messages from a queue
# r = requests.get("{}/rabbit/TODO".format(APIENDPOINT))
# print("statut:{}".format(r.status_code))
# print(r.text)
