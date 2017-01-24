#! -*- coding:UTF-8 -*-

"""
logging support module
"""
import logging

def getLogger(name):
    logging.basicConfig()
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    return log
