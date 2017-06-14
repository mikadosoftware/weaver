
from github import Github
import time
import os
import pprint

'''
Notes
'''
gmail_app_specific_password = open("/home/pbrian/secure/github.password").read()
g = Github("lifeisstillgood", gmail_app_specific_password)

def showrepos():
    for repo in g.get_user().get_repos():

#        if "salt" in repo.name:
#            import code;code.interact(local=locals())
        if repo.owner.login in (u"lifeisstillgood",
                                u'mikadosoftware') and not repo.fork:
            print "#", repo.name
            print "git clone %s" % repo.ssh_url


def repo_detail(repo_name):
    '''Assuming we find all the python repos (!)
       lets find out which are UK based / users
    '''
    r = g.get_repo(repo_name)
    return r

def extract_repo_details(repo_full_name):
    r1 = repo_detail(repo_full_name)
    users = r1.get_contributors()
    ct = 0
    for u in users:
        print ".",
        udict = {}
        udict['repo_full_name'] = repo_full_name
        udict['login'] = u.login
        udict['company'] = u.company
        udict['email']=u.email
        udict['location'] = u.location
        stored(udict)
        ct+=1
        if ct % 10 == 0:
            print "Sleeping"
            time.sleep(1) # try to throttle self

if __name__ == '__main__':
    showrepos()
