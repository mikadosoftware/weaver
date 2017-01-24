#!/bin/env python

import os, sys
from fnmatch import fnmatch

crap_matcher = ['*.*~', '*.pyc']
KILLFLAG=False



def killfiles(kill_list, flag=False):
    '''
    '''
    for fn in kill_list:
        if flag:
            os.remove(fn)
            print "[x] ", fn
        else:
            print "[ ] ", fn

def clean_tree(cwd=None, killflag=False):
    '''walk eveything below me, delete all the crap
    '''
    rdir = cwd or os.getcwd()
    kill_list = []
    for root, dirs, files in os.walk(rdir):
        if ".git" in dirs:
            dirs.remove(".git")

        for file in files:
            for pattern in crap_matcher:
                if fnmatch(file, pattern):
                    kill_list.append(os.path.join(root, file))
    killfiles(kill_list, killflag)

WEAVER_ENTRY_POINTS=[clean_tree]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
