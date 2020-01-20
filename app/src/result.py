import json
import os
import random
import time
import requests

APIENDPOINT = "http://127.0.0.1:5000"
WAITING_DELAY = 30

hasResult = True
result = 0
while hasResult:
    r1 = requests.get("{}/rabbit/get/DONE".format(APIENDPOINT))
    nbr_result = int(r1.text)

    if (nbr_result > 0):
    #   r2 = requests.get("{}/rabbit/n_ack/DONE".format(APIENDPOINT))
        if (nbr_result >= 4):
            r2 = requests.get("{}/rabbit/DONE".format(APIENDPOINT))
            data = json.loads(r2.text)
            print(data)
        else: 
            print ("Pas encore terminée.")

    else: 
        time.sleep(WAITING_DELAY)