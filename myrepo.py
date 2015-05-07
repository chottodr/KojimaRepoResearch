#!/usr/bin/env python
# -*- coding: utf-8 -*-
#myrepo.py

from github import Github
import getpass


gusername = raw_input("Github_ID>")
gpassword = getpass.getpass()

g = Github(gusername,gpassword)

#export repositories name
for repo in g.get_user().get_repos():
    print "{",
    print repo.name
    print repo.id,
    print "}"
