#!/usr/bin/env python

from setuptools import setup, find_packages

def get_version():
    return open("VERSION").read().strip()


setup(
    name='Weaver',
    version=get_version(),
    description='Weaver tries to wrap fabric and emulate a mini ansible.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'weaver = weaver.weaver:main',
        ]
    },
    
)
