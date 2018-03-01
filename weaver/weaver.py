docopt_str = """Weaver

Usage:
  weaver todo  [<rootpath>]
  weaver clean [<rootpath>]
  weaver touchpad
  weaver fab [<commandstr>...]
  weaver newfile [<filename>]
  weaver (-h | --help)
  weaver --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt

'''
weaver
------

I want to have a single dev-helper tool plus a stringent dev process.
So I want weaver.  It will act a little bit like phab in phabricatgor - a local
command line tool that will enforce local operations.

Things I want as a develeoper

* Linting tool
* testing tool - py.test that can use doctests as well as others
* todoinator
* linking todos to longer term store
* code-forensics?
* build tool
* laptop build tool
* test coverage
* how to do micking??


# todo:: set up weaver project files, including
       making weavier requirments.txt use -e git:/// for mikadolib
       so there is a decent loop for development

# todo:: have weaver clone me all my repos from specific github

# todo:: have weaver build new project / repos

# todo:: have weaver build a todoinator

#todo:: have weaver do the devclean function

#todo:: todo-inator can smmothly show me todos in a file,
       can give those todos a uuid, and then can look for todo.txt files
       which map more detail from todo id onto file and even todo/ dir which
       holds those uuids as text files for really detailed discussions
       We can even extend the idea to subject files of emails, or god help us IRC

#todo: create a useful plugin approach for weaver - so can use the
      code from imorted modules... ???
'''
from fabric.api import local, env, run, sudo
from fabric.tasks import execute
import fabric.contrib.files

# fab modules I have written that make a little library
from weaver.fabmodules import fedorafab
from weaver.fabmodules import fab_terminal_setup
from weaver.fabmodules.fab_misc import *




from .devtools import xtools
def touchpad():
    xtools.touchpad()

from .devtools import devclean
def clean(rootpath):
    devclean.clean_tree(rootpath, killflag=True)

from .devtools import todoinator
def todo_tree(rootpath):
    todoinator.parse_tree(rootpath)

def weaver_newfile(filename):
    ''' '''
    tmpl = u'''#!/bin/env python
#! *-* coding:utf-8 *-*


'''
    open(filename).write(tmpl)
    
    
def fab_runner2(commandin=None):
    """Can I run fab commands direct?
    
    """
    fedorafab.setup()
    
    #test only
    print("ABout to run test_fab <{0}>".format(commandin))
    val = execute(fab_terminal_setup.test_fab,
            hosts=['127.0.0.1',]) #any args kwds in execute get passed to taskfn
    
    print("Val was {0}".format(val))

def linteretc():
    """
    """
    #We want to collect and then test and run lint and other
    #QA tools across the whole /projects/ setup.
    pass

def main():
    args = docopt(docopt_str)

    if args['<rootpath>'] and args['todo']:
        print("starting todo")
        todo_tree(args['<rootpath>'])


    if args['<rootpath>'] and args['clean']:
        print("starting clean")
        clean(args['<rootpath>'])


    if args['<commandstr>'] and args['fab']:
        print("starting fab")
        fab_runner2(args['<commandstr>'])

    if args['<filename>'] and args['newfile']:
        print("creating new file")
        weaver_newfile(args['<filename>'])
        
    if args['touchpad']:
        touchpad()


if __name__ == '__main__':
    main()
