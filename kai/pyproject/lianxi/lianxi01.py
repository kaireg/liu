#!/usr/bin/env python
#liu coding:utf-8 liu

def get_fundoc(func):
    #判断函数是否有文档描述，有则返回文档内容，没有则返回not，found
    if func.__doc__ == None:
        return "not,fund"
    else:
        return func.__doc__
import os
get_fundoc(get_fundoc)
get_fundoc(os)

def get_cjsum():
    #定义初始值为0，用for遍历1到100的数字，计算出1-100的平房和
    num1 = 0
    for i in range(1,101):
        num1 = num1 + i**2
    return num1
print get_cjsum()

