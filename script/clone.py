#!/usr/bin/env python
import os
import sys

def clone(repo):
    url = "https://github.com/"
    git =".git"
    os.chdir("repositories")
    dir_name = repo.replace("/","_")
    os.mkdir(dir_name)
    os.chdir(dir_name)
    os.system("git clone "+url+repo+git)

if __name__ =="__main__":

    argvs = sys.argv
    repo = argvs[1]
    clone(repo)
