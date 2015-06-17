#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from github import Github
from pymongo import Connection

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
###############################################
#*sha
#*commit--author
#       |_commiter
#       |_message
#more detail in
#https://developer.github.com/v3/repos/commits/
###############################################

#connection
connect = Connection('localhost',27017)
#dbの呼び出し
db = connect.test
#collection(table)の呼び出し(同時に初期化)
col = db.commit
col.drop()

#get all revisions (commits)
revision = repo.get_commits()
n=0
print "takeing commit message..."
for rev in revision:
    #取得した各リビジョンに有る情報をDBに格納
    col.save({'SHA':rev.sha,'message':rev.commit.message.encode('utf-8')})
    n = n+1
    print "insert commit to db no.",
    print n
    #print rev.commit.message.encode('utf-8')
