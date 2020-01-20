#!/usr/bin/python3
# Code du commanditaire
import requests
import json
import os
import random
import time
from mygit import git_add_file, git_commit, git_push, git_init, git_pull

APIENDPOINT = "http://127.0.0.1:5000"
basepath = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(os.path.dirname(basepath))

# création des tâches sous format JSON

# Cette partie du code commanditaire permet de distribuer les tâches
echiquier = int(
    input("Pour quel type d'échiquier aimeriez-vous avoir le nombre de solutions: "))
_dispatch = input('Voulez-vous diviser la tâche (o/n): ')
if _dispatch == 'o':
    nbr_task = int(input('En combien de tâches: '))
    p_name = input('Entrer le nom de votre projet: ')
pid = random.randrange(0, 1000, 2)
p_file_params = '{}_parameters.txt'.format(p_name)
stream1 = os.popen('touch param/{}'.format(p_file_params))
stream1.read()

params = []
for i in range(nbr_task):
    param = {}
    _id = i+1
    task = {
        "pid": pid,
        "id": _id,
        "code": "https://raw.githubusercontent.com/essossolam/dev_rt0704/master/app/src/code/ndame.py",
        "params": "https://raw.githubusercontent.com/essossolam/dev_rt0704/master/app/src/param/{}".format(p_file_params),
        "file_name": p_file_params
    }

    #[POST] envoie des tâches dans a file de message 'TODO'
    payload= {}
    payload['task'] = task
    mydata = {"data": json.dumps(payload)}
    r = requests.post("{}/rabbit/{}".format(APIENDPOINT,'TODO'), data=mydata)
    print("statut:{}".format(r.status_code))
    print(r.text)

    #paramètre pour chaque tâche créée
    param['pid'] = pid
    param['task_id'] = _id
    param['input'] = int(echiquier/nbr_task)
    params.append(param)

    # print(task)
data = {}
data['task_param'] = params


def write_f_parameters(file_name, _data):
    file = open('param/{}'.format(file_name), 'w')
    file.write(json.dumps(_data))
    file.close


write_f_parameters(p_file_params, data)

# Envoie des paramètres sur git
git_add_file("{}/param/{}".format(basepath, p_file_params), parentDir)
git_commit(parentDir, "The {} project parameters".format(p_name))
git_push(parentDir)

# Envoie du code sur git
git_add_file("{}/code/ndame.py".format(basepath), parentDir)
git_commit(parentDir, "The damen problem code")
git_push(parentDir)
# git_init()
# POST create new queue
# payload= {}
# queue1 = 'TODO'
# queue2 = 'DONE'
# payload['queue_name'] = queue1
# mydata = {"data": json.dumps(payload)}
# r = requests.post("{}/rabbit".format(APIENDPOINT), data=mydata)
# print("statut:{}".format(r.status_code))
# print(r.text)

# POST insert new message in queue
# queue1 = 'TODO'
# queue2 = 'DONE'


# #GET messages from a queue
# r = requests.get("{}/rabbit/TODO".format(APIENDPOINT))
# print("statut:{}".format(r.status_code))
# print(r.text)
