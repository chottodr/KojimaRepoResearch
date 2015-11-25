#!/usr/bin/env python
# -*- coding: utf-8 -*-
#makedocument_ns.py
###example################################
#python makedocument_ns.py directory_path
##########################################
import sys
from github import Github

#get token
t = open('token','r')
token = t.read()
token = token.rstrip('\n')

#Create GitHub INSTANCE
g = Github(token)
t.close()

#show repositoory from repository fullname
repo_name = raw_input("Repository_Name>")

#take repository info
repo = g.get_repo(repo_name)

argvs = sys.argv
try:
    path = argvs[1]
except IndexError:
    print "please specify directory path to save txt file!!"
    sys.exit()

doc = open(path+'/repo_files.txt','w')
revision = repo.get_commits()
n=0
for rev in revision:
    n=n+1
    print "commit..."
    print n
    doc.write(rev.commit.message.encode('utf-8').replace("\n",""))
    doc.write("\n")
    if n == 50:
        break

