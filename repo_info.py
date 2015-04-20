#repo_info.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from github import Github
import getpass
gusername = raw_input("Github_ID>")
gpassword = getpass.getpass()

g = Github(gusername,gpassword)

#show repositoory from repository fullname
repo_name = raw_input("Repository_Name>")

repo = g.get_repo(repo_name)
print "Owner:",
print repo.owner.name
print "Repositoty ID:",
print repo.id

