#!/usr/bin/env python
#liu coding:utf-8 liu

def func(a1,a2,a3):
    return a1+a2+a3

#查看函数有哪些属性
dir(func.__code__)

global arg
arg = 3

def get_func():
    global arg
    arg = 1
    return arg
get_func()
print arg


#程序开始    类似于 c语言的  void main()
if __name__ ==  '__main__':
    print dir(func.__code__)
    print get_func()

