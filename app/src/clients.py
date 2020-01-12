#!/usr/bin/python3
#Code du commanditaire 
import requests
import json
from mygit import git_add_file, git_commit, git_push, git_init, git_pull

APIENDPOINT = "http://127.0.0.1:5000"

#création des tâches sous format JSON
task = {
    "pid":1,
    "id":1,
    "code":"https://github.com/essossolam/rt0704",
    "params":"https://github.com/essossolam/rt0704"
}
#Envoie des paramètres sur git
#Envoie du code sur git
# git_add_file("/home/jordy/dev_folder/rt0704/ndame.py","/home/jordy/dev_folder/rt0704")
# git_commit("/home/jordy/dev_folder/rt0704","The damen problem code 3")
# git_push("/home/jordy/dev_folder/rt0704")
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
payload= {}
queue1 = 'TODO'
queue2 = 'DONE'
payload['task'] = task
mydata = {"data": json.dumps(payload)}
r = requests.post("{}/rabbit/{}".format(APIENDPOINT,queue1), data=mydata)
print("statut:{}".format(r.status_code))
print(r.text)


# #GET messages from a queue
# r = requests.get("{}/rabbit/TODO".format(APIENDPOINT))
# print("statut:{}".format(r.status_code))
# print(r.text)
