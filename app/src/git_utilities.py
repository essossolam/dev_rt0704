import requests
import json
import os
import random
import time
from mygit import git_add_file, git_commit, git_push, git_init, git_pull


# Envoie des paramètres sur git
    git_add_file("{}/param/{}".format(sys.argv[1], sys.argv[2]), sys.argv[3])
    git_commit(sys.argv[3], "The {} project parameters".format(sys.argv[4]))
    git_push(parentDir)

    # Envoie du code sur git
    git_add_file("{}/code/ndame.py".format(sys.argv[1]), sys.argv[3])
    git_commit(sys.argv[3], "The damen problem code")
    git_push(sys.argv[3])