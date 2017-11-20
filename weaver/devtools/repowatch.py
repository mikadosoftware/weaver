
from github import Github
import time
import os
import pprint
import getpass

'''
Repo Watch is a simple exercise to keep my local laptop 
synchronised with the ridiculous number of repos I keep creating 
'''

def showrepos():
    print("Called")
    github_password = getpass.getpass('Github password: ')
    g = Github("lifeisstillgood", github_password)

    for repo in g.get_user().get_repos():

#        if "salt" in repo.name:
#            import code;code.interact(local=locals())
        if repo.owner.login in ("lifeisstillgood",
                                'mikadosoftware') and not repo.fork:
            print("#", repo.name)
            print("git clone %s" % repo.ssh_url)

if __name__ == '__main__':
    showrepos()
