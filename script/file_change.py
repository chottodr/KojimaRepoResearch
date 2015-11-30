#!/usrbin/env python
import os
import sys

def file_change(repo):
    dir_name = repo.replace("/","_")
    os.chdir("repositories/"+dir_name)
    os.system('git log --reverse --date=short --no-merges --numstat --pretty=format:"%cd" > FileChange.txt')

if __name__ =="__main__":
    argvs = sys.argv
    repo = argvs[1]
    file_change(repo)
