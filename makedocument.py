#!/usr/bin/env python
# -*- coding: utf-8 -*-
#makedocument.py

from github import Github

#get token
t = open('token','r')
token = t.read()
token = token.rstrip('\n')

#Create GitHub INSTANCE
g = Github(token)
t.close()

#show repositoory from repository fullname
repo_name = "ruby/ruby"#raw_input("Repository_Name>")

#take repository info
repo = g.get_repo(repo_name)

doc = open('repotxt/repo_files.txt','w')
revision = repo.get_commits()
n=0
for rev in revision:
    n=n+1
    print "commit...",
    print n
    doc.write(rev.commit.message.encode('utf-8').replace("\n",""))
    doc.write(" ")
    files = repo.get_commit(rev.sha).files
    for f in files:
        doc.write(f.filename.encode('utf-8'))
        doc.write(" ")
        doc.write(f.status)
        doc.write(" ")
    doc.write("\n")
    if n == 50:
        break

