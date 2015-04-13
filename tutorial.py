from github import Github
import getpass
gusername = raw_input("Github_ID>")
gpassword = getpass.getpass()
g = Github(gusername,gpassword)

#export repository
for repo in g.get_user().get_repos():
    print repo.name

