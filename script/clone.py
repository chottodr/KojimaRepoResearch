#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def clone(repo):#管理ディレクトリにリポジトリのクローン
    url = "https://github.com/"
    git =".git"
    os.chdir("repositories")
    dir_name = repo.replace("/","_")
    os.mkdir(dir_name)
    os.chdir(dir_name)
    os.system("git clone "+url+repo+git)
    os.chdir("../../")

def summaries(repo):#管理ディレクトリにリポジトリのコミットメッセージを設置
    dir_name = repo.replace("/","_")
    tmp = repo.split("/")
    repo_name = tmp[-1]
    os.chdir("repositories/"+dir_name+"/"+repo_name)
    os.system('git log --reverse --oneline --no-merges --pretty=format:"%s" > ../CommitMessage.txt')
    os.chdir("../../../")


def SHA(repo):#管理ディレクトリにリポジトリのSHAを設置
    dir_name = repo.replace("/","_")
    tmp = repo.split("/")
    repo_name = tmp[-1]
    os.chdir("repositories/"+dir_name+"/"+repo_name)
    os.system('git log --reverse --no-merges --pretty=format:"%H" > ../SHA.txt')
    os.chdir("../../../")

def source_line(repo): 
    dir_name = repo.replace("/","_")
    tmp = repo.split("/")
    repo_name = tmp[-1]
    os.chdir("repositories/"+dir_name+"/"+repo_name)
    if(os.path.exists("../source_Lines")==False):
        os.mkdir("../source_Lines")
    sha = open("../SHA.txt","r").read().split("\n")
    i = 0
    for shash in sha:
        os.system('git checkout '+shash)
        os.system('wc -l `find * -type f` > ../source_Lines/'+str(i)+'.txt')
        i = i+1
    print "Done"


if __name__ =="__main__":

    argvs = sys.argv
    repo = argvs[1]
    clone(repo)
    summaries(repo)
    SHA(repo)
    source_line(repo)

