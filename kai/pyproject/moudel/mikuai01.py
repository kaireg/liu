#!/usr/bin/env python
# coding:utf-8

#模块的导入方式


#直接导入整个模块,调用时需要加上模块名
import os
# os.open()

#导入模块中的某个方法，调用时直接使用，无需加上模块名
from random import seed
# print seed

#导入整个模块，调用时直接使用该模块的__all__里所定义的方法，无需加上那个模块名
from urllib import *



