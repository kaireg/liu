#!/usr/bin/env python
# liu coding:utf-8 liu


#唉，还是太菜，用这种愚蠢的方法
def func(*num):
    list_a = list(num)
    list_a.sort()
    b = len(list_a)
    return list_a[0],list_a[b-1]
func(123,234,345,678,987,765)


#使用内置的max，min的方法直接求出最大值，最小值，同时还可以判断参数类型
def func1(*nmm):
    for i in nmm:
        if not isinstance(i,int):
            return '参数错误，参数必须为整数'
    return max(nmm),min(nmm)
func1(123,234,345,678,987,765)

def func2(*stt):
    # 创建一个空的列表，以装载字符串长度
    list = []
    for i in stt:
        if not isinstance(i,str):
            return '参数错误，参数必须为字符串'
        # 计算每个字符串的长度并且加入列表
        list.append(len(i))
    # 计算字符串长度列表中最大值即为最长的字符串所在列表中的位置（3），通过index索引找到这个字符串，并输出
    return stt[list.index(max(list))]
func2("zhangfei","lubu","liubei","liujinkai","guanyu")

#调用模块帮助文档
def get_doc(modu):
    return modu.__doc__
import os
get_doc(os)

#查看某个文件内容
def get_text(f):
    filen = file(f,'r')
    return filen.read()
get_text('E:\python\py\liu.txt')



import glob

def get_dir(d):
    for i in glob.glob(d + '\*'):
        return i
get_dir("E:\python\py")
