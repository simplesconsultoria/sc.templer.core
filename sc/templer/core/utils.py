# -*- coding:utf-8 -*-
import os
from datetime import datetime


def gen_version():
    ''' Generates a version number based on YYYYMMDD.nn pattern'''
    return datetime.now().strftime('%Y%m%d.01')


def remove_egg_docs(path):
    ''' Remove original egg_docs structure files '''
    FILES = ['CHANGES.txt', 'CONTRIBUTORS.txt', 'README.txt', ]
    for FILE in FILES:
        os.remove(os.path.join(path, FILE))
