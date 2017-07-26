#!/usr/bin/env python
#coding:utf-8

'''
对装饰器的简单理解
'''


import time

def timeit(func):

    def warps():
        start = time.clock()
        func()
        end = time.clock()
        print "花费时间：" , end-start
    return warps

#foo = timeit(foo)

@timeit
def foo():
    time.sleep(1)
    print 'hello,world'

foo()

def dectr(func):

    def bbc():
        print '这是第一个装饰器 start'
        func()
        print '这是第一个装饰器 end'
    return bbc

def decto(func):

    def bbb():
        print '这是第二个装饰器 start'
        func()
        print '这是第二个装饰器 end'
    return bbb

#这里demo = dectr(decto(demo))  顺序很重要

@dectr
@decto
def demo():
    print 'biubiubiu'

demo()