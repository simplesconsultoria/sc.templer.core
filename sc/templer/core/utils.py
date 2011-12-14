# -*- coding:utf-8 -*-
import os
from datetime import datetime


def gen_version(show_minor=True):
    ''' Generates a version number based on YYYYMMDD.nn pattern'''
    version = datetime.now().strftime('%Y%m%d')
    minor = ''
    if show_minor:
        minor = '.01'
    return '%s%s' % (version, minor)


def remove_egg_docs(path):
    ''' Remove original egg_docs structure files '''
    FILES = ['CHANGES.txt', 'CONTRIBUTORS.txt', 'README.txt', ]
    for FILE in FILES:
        os.remove(os.path.join(path, FILE))


def year():
    ''' Return the actual year '''
    return datetime.now().strftime('%Y')
