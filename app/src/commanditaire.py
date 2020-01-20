import requests
import json
import os
import random
import time
from mygit import git_add_file, git_commit, git_push, git_init, git_pull

APIENDPOINT = "http://127.0.0.1:5000"

r = requests.get("{}/rabbit/get/DONE".format(APIENDPOINT))
print("statut:{}".format(r.status_code))
print(r.text)