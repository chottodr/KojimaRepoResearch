#!/usr/bin/env python
# -*- coding: utf-8 -*-
#makedocument_ns.py
##################
#実行例 makedocument_fun.py 保存ディレクトリpath
#
#################
import sys
from github import Github
import MeCab

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
    if rev.author is None:
        m = MeCab.Tagger("-Ochasen")
        node = m.parseToNode(rev.commit.message.encode("utf-8").replace("\n",""))
        while node:
            if node.feature.split(".")[0] == "名詞":
                print node.surface
                doc.write(node.surface)
        doc.write("\n")

