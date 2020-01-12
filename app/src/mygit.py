#!/usr/bin/python3

from git import Repo, Git
import os

def git_init():
    bare_repo = Repo.init(os.path.join('/home/jordy', 'dev_folder'), bare=True)
    assert bare_repo.bare

def git_clone(repo_url, repo_dir, ref='master'):
    repo = Repo.clone_from(repo_url, repo_dir)
    repo.remotes.origin.fetch(ref)
    g = Git(repo.working_dir)
    #g.checkout('FETCH_HEAD')

def git_pull(repo_dir, ref='master'):
    repo = Repo(repo_dir)
    repo.remotes.origin.pull(ref)

def git_add_file(new_file,repo_dir):
    repo = Repo(repo_dir)
    repo.git.add(new_file)

def git_add_all_file(repo_dir):
   repo = Repo(repo_dir)
   repo.git.add(all=True)

def git_commit(repo_dir, c_message):
    repo = Repo(repo_dir)
    repo.git.commit('-m',c_message,author='essossolam@github.com')

def git_push(repo_dir, ref='master'):
    repo = Repo(repo_dir)
    repo.remotes.origin.push(ref)


#git_clone('https://github.com/essossolam/rt0704','/home/jordy/dev_folder/rt0704')
#git_add_all_file('/home/jordy/dev_folder/rt0704')
#git_commit('/home/jordy/dev_folder/rt0704','new file')
#git_pull('https://github.com/essossolam/rt0704')
#git_push('/home/jordy/dev_folder/rt0704')
#git_init()
