#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from fabric.api import local, env, run, sudo
from fabric.tasks import execute
import fabric.contrib.files
from fabric.context_managers import settings
import sys
import requests

"""
=====
Notes
=====

I am using fab as a base for a ansible-like but very simple local control
system.
It will enable me to manage the local workstation, and to configure remote
docker instances.

* env.hosts is set to be my local machine by default.
  how to configure that?

* whats the main approach - lots of small modules doing things, ala salt?

Keeping my *own* laptop uptodate

fab install_terminal will login to my local laptop and sudo install the instructiones below.
I need a means to flip that in weaver...


---------------
Features wanted
---------------

* ability to change config files to how I want.
  initial cut - just keep local copy of what I want and push it,
  May have versioning issues.
  is much much simpler

  ALternatively something that programmatically allows line changes etc etc


    sudo('whoami', user='pbrian')
    #we want to have a nice set of dotfiles, at same time as prepping the packages etc
    with settings(sudo_user='pbrian'):
        sudo("git init --bare $HOME/.cfg")
        sudo("touch $HOME/.cfg/junk")
        sudo("alias homegit='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'")
        sudo("/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME config --local status.showUntrackedFiles no")
        #this needs something else
        sudo('''echo "alias homegit='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'" >> $HOME/.bashrc''')


"""

import tempfile, io
from fabric.api import get, put, settings

#: run locally
env.hosts = ['127.0.0.1']

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def init_homedir():
    '''Set up a git repo "next" to home, and use to track home dir changes.
    
    we hsall have a command homegit that just operates on the home dir.
    we need to get that local bare directory sent upto github somehow.

    '''
    sudo('whoami', user='pbrian')
    #we want to have a nice set of dotfiles, at same time as prepping the packages etc
    with settings(sudo_user='pbrian'):
        sudo("git init --bare $HOME/.cfg")
        sudo("touch $HOME/.cfg/junk")
        sudo("alias homegit='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'")
        sudo("/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME config --local status.showUntrackedFiles no")
        #this needs something else
        sudo('''echo "alias homegit='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'" >> $HOME/.bashrc''')

def install_sshd():
    """
    """
    sshd_config_path = "/etc/ssh/sshd_config"
    #sshd MUST be installed previously by BASH else fabric cannot sudo in locally
    #: configure
    fabric.contrib.files.append(sshd_config_path,
                                "# Configured by weaver.",
                                use_sudo=True)

def install_docker():
    """
    NB fixed on a specific version of Docker.
    Upgrade carefully.


    https://docs.docker.com/engine/installation/linux/ubuntulinux/#install-a-specific-version
    """
    sudo("apt-get update")
    sudo("apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D")
    sudo("apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'")
    sudo("apt-get update")
    sudo("apt-cache policy docker-engine")
    sudo("apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual")
    sudo("apt-get install -y docker-engine=1.12.4-0~ubuntu-xenial")

def install_atom():
    url = 'https://github.com/atom/atom/releases/download/v1.12.5/atom-amd64.deb'
    #pkg = download_file(url)
    pkg = '/home/pbrian/projects/weaver/atom-amd64.deb'
    local("sudo dpkg --install %s" % pkg)

def remove_atom():
    sudo("dpkg --remove %s" % pkg)

def install_xfce4():
    sudo("apt-get update")
    sudo("apt-get install -y xfce4")
    sudo("apt-get install -y lubuntu-desktop")

def install_dropbox():
    """
    # install drop box on local linux box
    cd /tmp
    wget https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2015.10.28_amd64.deb .
    sudo apt-get install python-gtk2 libpango1.0-0

    """
    sudo("yum install -y pygtk2")
    sudo("yum install -y pango")
    tmpfile = "/tmp/dropboxfoo.rpm"
    sudo("wget -O %s https://www.dropbox.com/download?dl=packages/fedora/nautilus-dropbox-2015.10.28-1.fedora.x86_64.rpm " % tmpfile)
    sudo("yum localinstall -y %s" %  tmpfile)
    #this installs a helper app - to actually install daemon run
    #dropbox start -i ... which will run some UI for manual install

def test_fab():
    """
    """
    sudo("touch /home/pbrian/foo.txt")
    sudo("ls -l /home/pbrian/foo.txt")
    

class RemoteException(Exception):
    """
    """
    pass

def log(txt):
    print(txt)

def read_remote_file(remote_path):
    """read back a remote file. Assume it is UTF-8 encoded "plain" text
    """

    with settings(abort_exception=RemoteException):
        with tempfile.TemporaryFile() as fd:
            get(remote_path, fd)
            fd.seek(0)
            content=fd.read()
            content = content.decode('utf-8')
    return content

def put_remote_file(remote_path, content):
    """
    """
    with settings(abort_exception=RemoteException):
        fd = io.StringIO()
        fd.write(content)
        put(fd, remote_path)
        

def edit_remote_file(remote_path,
                     lines_to_append=None,
                     lines_to_delete=None):
    """
    """
    try:
        content = read_remote_file(remote_path)
    except RemoteException:
        log("could not read {0}".format(remote_path))
        content = ''
#    content += "\n#/weaver\n"
    content += lines_to_append 
#    content += "\n#weaver/\n" # removed cos .Xresoucres demands ! comment symbol
    put_remote_file(remote_path, content)


def replace_remote_file(remote_path,
                     lines_to_append=None,
                     lines_to_delete=None):
    """
    """
    content = ''
    content += lines_to_append 
    put_remote_file(remote_path, content)
    
    
def common_utilities():
    """Common utilities I just want to add
    """
    utils = ['shutter']
    for util in utils:
        sudo("yum install -y {0}".format(util))
