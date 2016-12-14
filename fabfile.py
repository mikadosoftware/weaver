from fabric.api import local, env, run, sudo
from fabric.tasks import execute
import fabric.contrib.files
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

---------------
Features wanted
---------------

* ability to change config files to how I want.
  initial cut - just keep local copy of what I want and push it,
  May have versioning issues.
  is much much simpler

  ALternatively something that programmatically allows line changes etc etc




"""

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
    """
    sudo("apt-get update")
    sudo("apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D")
    sudo("apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'")
    sudo("apt-get update")
    sudo("apt-cache policy docker-engine")
    sudo("apt-get install -y docker")

def install_atom():
    url = 'https://github.com/atom/atom/releases/download/v1.12.5/atom-amd64.deb'
    #pkg = download_file(url)
    pkg = '/home/pbrian/projects/weaver/atom-amd64.deb'
    local("sudo dpkg --install %s" % pkg)

def remove_atom():
    sudo("dpkg --remove %s" % pkg)
