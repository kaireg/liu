#!/usr/bin/env python
#liu coding:utf-8 liu

import logging

logger = logging.getLogger()

hdlr = logging.FileHandler('log.txt')

formatter = logging.Formatter('%(asctime)s %(filename)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr)

logger.setLevel(logging.NOTSET)

class fileinfo(object):

    def __init__(self,filename):
        self.filename = filename

    def __enter__(self):
        try:
            a = open(self.filename, 'r')
        except:
            print u"你输入的文件名无效"
        else:
            return a.read()

    def __exit__(self,type,value,traceback):
        logger.error(self.filename)

with fileinfo('E:\python\pyproject\conf.txt') as b:
    pass