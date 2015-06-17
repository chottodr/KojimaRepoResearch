#!/usr/bin/env python
# -*- coding: utf-8 -*-
#file_changes.py

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

tsv = open('repotxt/repo_files.tsv','w')
revision = repo.get_commits()
n=0
for rev in revision:
    n=n+1
    print "Revision...",
    print n
    if rev.author is None:
        files = repo.get_commit(rev.sha).files
        for f in files:
            tsv.write(f.filename)
            tsv.write("\t")
            tsv.write(str(f.changes))
            tsv.write("\n")

