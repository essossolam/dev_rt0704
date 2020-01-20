#!/usr/bin/python3
# Code du commanditaire

import requests
import json
import os
import random
import time
from mygit import git_add_file, git_commit, git_push, git_init, git_pull

WAITING_DELAY = 30
APIENDPOINT = "http://127.0.0.1:5000"
basepath = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(os.path.dirname(basepath))

""" Début déclarations des fonctions
"""

def create_queues_for_project():
    #POST create new queue
    payload= {}
    queue = ['TODO', 'DONE']
    for q in queue:
        payload['queue_name'] = q
        mydata = {"data": json.dumps(payload)}
        r = requests.post("{}/rabbit".format(APIENDPOINT), data=mydata)
        print("statut:{}".format(r.status_code))
        print(r.text)

def write_f_parameters(file_name, _data):
    file = open('param/{}'.format(file_name), 'w')
    file.write(json.dumps(_data))
    file.close

def write_in_logs(message):
    payload= {}
    payload['message'] = message
    mydata = {"data": json.dumps(payload)}
    r = requests.post("{}/rabbit/logs/{}".format(APIENDPOINT,'logs'), data=mydata)

def git_utilities(basepath, p_file_params, parentDir, p_name):
    # Envoie des paramètres sur git
    add1 = git_add_file("{}/param/{}".format(basepath, p_file_params), parentDir)
    commit1 = git_commit(parentDir, "The {} project parameters".format(p_name))
    push1 = git_push(parentDir)

    # Envoie du code sur git
    add2 = git_add_file("{}/code/ndame.py".format(basepath), parentDir)
    commit2 = git_commit(parentDir, "The damen problem code")
    push2 = git_push(parentDir)

    return True

""" Fin déclarations des fonctions
"""
# création des tâches sous format JSON

# Cette partie du code commanditaire permet de distribuer les tâches
echiquier = int(
    input("Pour quel type d'échiquier aimeriez-vous avoir le nombre de solutions: "))
_dispatch = input('Voulez-vous diviser la tâche (o/n): ')

if _dispatch == 'o':
    nbr_task = int(input('En combien de tâches: '))
    p_name = input('Entrer le nom de votre projet: ')

#Appel de la fonction pour créer les files de messages
create_queues_for_project()

pid = random.randrange(0, 1000, 2)
p_file_params = '{}_parameters.txt'.format(p_name)
stream1 = os.popen('touch param/{}'.format(p_file_params))
stream1.read()

params = []
pending_tasks = {}
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
    payload = {}
    payload['task'] = task
    pending_tasks[(pid+_id)] = task
    mydata = {"data": json.dumps(payload)}
    r = requests.post("{}/rabbit/{}".format(APIENDPOINT,'TODO'), data=mydata)
    print("statut:{}".format(r.status_code))
    print(r.text)
    write_in_logs("La tâche {} du projet numero {} a été envoyée.".format(_id, pid))

    #paramètre pour chaque tâche créée
    param['pid'] = pid
    param['task_id'] = _id
    param['input'] = int(echiquier/nbr_task)
    params.append(param)

    # print(task)
data = {}
data['task_param'] = params

write_f_parameters(p_file_params, data)

hasResult = True
result = 0

try:
    git_utilities(basepath, p_file_params, parentDir, p_name)
except:
    while hasResult: 
        r = requests.get("{}/rabbit/get/DONE".format(APIENDPOINT))
        nbr_result = int(r.text)

        if (nbr_result > 0):
            if (nbr_result == nbr_task):
                are_get = True
                while are_get:
                    r2 = requests.get("{}/rabbit/DONE".format(APIENDPOINT))
                    if (r2.text != '0'):
                        data = json.loads(r2.text)
                        result += int(data['solutions'])
                    else:
                        are_get = False
                        hasResult = False    
                        print("Tout les jobs sont terminées !!!... \n")      
                        print("Le nombre de solutions possible est : {}".format(result))
            else:
                time.sleep(WAITING_DELAY)
                r4 = requests.get("{}/rabbit/get/DONE".format(APIENDPOINT))
                nbr_result2 = int(r.text)
                for i in range(nbr_result2):
                    r3 = requests.get("{}/rabbit/n_ack/DONE".format(APIENDPOINT))
                    data2 = json.loads(r3.text)
                    _key = int(data2['id']) + int(data2['pid'])
                    print (pending_tasks)
                    del pending_tasks[key]
                    if (len(pending_tasks)!= 0):
                        for item in pending_tasks.items():
                            payload = {}
                            payload['task'] = item
                            mydata = {"data": json.dumps(payload)}
                            r5 = requests.post("{}/rabbit/{}".format(APIENDPOINT,'TODO'), data=mydata)


        else: 
            time.sleep(WAITING_DELAY)




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

#Récupération des résultats

#Gestion de la panne
