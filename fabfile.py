from fabric.api import local, env, run, sudo
from fabric.tasks import execute
import fabric.contrib.files

# fab modules I have written that make a little library
from fabmodules.fedorafab import *
from fabmodules.fab_terminal_setup import *


# todo: bootstrap laotop from scratch again
# todo: build book on weaver?
# todo: use weaver as a release on normal or a dev venv???
