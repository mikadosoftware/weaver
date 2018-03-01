
'''
We want to use the weaver fab lib to run a basic install, on my
laptop, of the terminal settings defined in here.

'''

from . import fedorafab
from .fedorafab import run, sudo

__all__ = ['domisc',]

def domisc():
    xpdf()


def xpdf():
    """
    """
    sudo("dnf install -y %s " % 'xpdf')
