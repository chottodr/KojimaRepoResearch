#!/usr/bin/env python
import os
import sys

def summaries(repo):
    dir_name = repo.replace("/","_")
    os.chdir("repositories/"+dir_name)
    os.system('git log --oneline --no-merges --pretty=format:"%s" > CommitMessage.txt')

if __name__ =="__main__":

    argvs = sys.argv
    repo = argvs[1]
    summaries(repo)
