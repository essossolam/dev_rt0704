import requests
import time
import json
import os

APIENDPOINT = "http://172.17.0.1:5000"
WAITING_DELAY = 30

def write_in_logs(message):
    payload= {}
    payload['message'] = message
    mydata = {"data": json.dumps(payload)}
    r = requests.post("{}/rabbit/logs/{}".format(APIENDPOINT,'logs'), data=mydata)

# def send_pending_task(task):
#     payload= {}
#     payload['task'] = task
#     mydata = {"data": json.dumps(payload)}
#     r = requests.post("{}/rabbit/{}".format(APIENDPOINT,'PENDING'), data=mydata)


def task_execution():
    # GET messages from a queue
    hasTask = True

    while hasTask:
        r = requests.get("{}/rabbit/TODO".format(APIENDPOINT))
        if (r.text != '0'):
            data = json.loads(r.text)
            #écriture dans la file logs lors de la réception de la tâche
            try: 
                write_in_logs("Tache {} recu.".format(data['id']))
                stream1 = os.popen('wget {}'.format(data['code']))
                stream1.read()
                stream2 = os.popen('wget {}'.format(data['params']))
                stream2.read()
                with open(data['file_name']) as json_file:
                    params = json.load(json_file)
                    for p in params['task_param']:
                        if (p['pid'] == data['pid'] and p['task_id'] == data['id']):
                            stream3 = os.popen('python ndame.py {} {} {}'.format(p['input'], p['pid'], p['task_id']))
                            output = stream3.read()
                            print(output)
                            #écriture dans la file logs lors de la fin de la tâche
                            write_in_logs("Tache {} du projet numero {} terminee et envoyee.".format(p['task_id'],p['pid']))
            except:
                hasTask = False
                send_pending_task(data)
                write_in_logs("Alert! un problème lors de l execution de la tahe {} du projet {} ".format(data['id'], data['pid']))
                break
        else:
            #temps d'attente pour aller chercher les tâches en cas d'un problème avec un autre worker
            time.sleep(WAITING_DELAY)

def run():
    start = time.time()
    task_execution()
    end = time.time()

run()