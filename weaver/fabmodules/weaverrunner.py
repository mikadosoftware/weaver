#

from fabric.tasks import execute
from fabric.api import local, env, run, sudo
#from weaver.fabmodules.fedorafab import test_fab
from fedorafab import test_fab

if __name__ == '__main__':
    env.host_string = '0.0.0.0'
    test_fab()
