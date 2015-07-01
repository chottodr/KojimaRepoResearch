#!/usr/bin/env python
# -*- coding: utf-8 -*-
#makedocument_ns.py

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

doc = open('repotxt_ns/repo_files_ns.txt','w')
revision = repo.get_commits()
n=0
for rev in revision:
    n=n+1
    doc.write(rev.commit.message.encode('utf-8').replace("\n",""))
    doc.write("\n")
    if n == 50:
        break

