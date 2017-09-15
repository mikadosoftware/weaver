docopt_str = """Weaver

Usage:
  weaver todo  [<rootpath>]
  weaver clean [<rootpath>]
  weaver touchpad
  weaver fab [<commandstr>...]
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
from .devtools import xtools
def touchpad():
    xtools.touchpad()

from .devtools import devclean
def clean(rootpath):
    devclean.clean_tree(rootpath, killflag=True)

from .devtools import todoinator
def todo_tree(rootpath):
    todoinator.parse_tree(rootpath)

import subprocess
def fab_runner(commandin=None):
    """
    if we see "fab xxx" then run the fab subprcess and return the data?
    issues:
    Build a very specific cmd for a subprocess.
    RUn the subprocess, and flash each popen line to out
    Beware - I miss the capture of the first line, so need to remeber to login 
 
    TODO: fix the specific config
    
    
    """
    venv_python = '/home/pbrian/venvs/weaver/bin/python'
    fabfilepath = '/home/pbrian/projects/weaver/fabfile.py'
    fabbin = '/home/pbrian/venvs/weaver/bin/fab'
    cmdlist = [venv_python, fabbin, '--fabfile=%s' % fabfilepath, commandin]
    try:
        p = subprocess.Popen(cmdlist,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT
                             )
        
        for line in iter(p.stdout.readline, b''):
            print(("> " + line.rstrip()))
            
    except subprocess.CalledProcessError as e:
        print("### Fab did not like the command")
        print(("# %s" % cmdlist))
        print("### and returned this")
        print((e.output))
        print("##########")
    
    
def main():
    args = docopt(docopt_str)
    
    if args['<rootpath>'] and args['todo']:
        print("starting todo")
        todo_tree(args['<rootpath>'])


    if args['<rootpath>'] and args['clean']:
        print("starting clean")
        clean(args['<rootpath>'])

    if len(args['<commandstr>'])>0 and args['fab']:
        print("starting fab")
        fab_runner(" ".join(args['<commandstr>']))

        
    if args['touchpad']:
        touchpad()


if __name__ == '__main__':
    main()
