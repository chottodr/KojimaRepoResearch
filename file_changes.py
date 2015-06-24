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
repo_name = "LightTable/Vim"#raw_input("Repository_Name>")

#take repository info
repo = g.get_repo(repo_name)

tsv = open('repotxt/repo_files.tsv','w')
revision = repo.get_commits()
n=0
f_l=[]
for rev in revision:
    n=n+1
    print "Revision...",
    print n
    files = repo.get_commit(rev.sha).files
    for f in files:
        f_l.append((f.filename.encode('utf-8'),f.changes,f.additions,f.deletions))


f_l = sorted(f_l)
for line in range(len(f_l)):
    for m in range(0,4):
        tsv.write(str(f_l[line][m]))
        tsv.write("\t")
    tsv.write("\n")
tsv.close
