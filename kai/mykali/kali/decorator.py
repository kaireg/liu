#!/usr/bin/env python
#coding:utf-8

# def demo1(func):
#     print "hello,world!"

def before():
    print 'before'

def after():
    print 'after'

def filter(before,after):
    def outer(main_func):
        def warpper(request,kargs):

            before(request,kargs)

            main_func(request,kargs)

            after(request,kargs)
        return warpper
    return outer

@filter(before,after)
def index():
    print 'index'

