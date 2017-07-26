#!/usr/bin/env python
#coding:utf-8

import threading
import time

def test(p):
    time.sleep(0.05)
    print p

ts = []

for i in xrange(0,10):
    th = threading.Thread(target=test,args=[i])
    th.start()
    ts.append(th)

# for i in ts:
#     i.join()

print "end!!!"

'''
习题一：已知列表 info = [1,2,3,4,55,233]

生成6个线程对象,每次线程输出一个值，最后输出

："the end"。
'''

info = [1,2,3,4,55,233]

def output(i):
    time.sleep(0.01)
    print info[i]

for i in xrange(0,6):
    th = threading.Thread(target=output,args=[i])
    th.start()

print " the end!"

'''
习题二：已知列表 urlinfo =

['http://www.sohu.com','http://www.163.com',

'http://www.sina.com'] 用多线程的方式分别打

开列表里的URL，并且输出对应的网页标题和内容。
'''
import urllib

urlinfo = ['http://www.sohu.com','http://www.163.com',
           'http://www.sina.com','http://www.liu.com']

def open_url(url):
    time.sleep(0.01)
    con = urllib.urlopen(url)
    print con.getcode()

for i in urlinfo:
    th = threading.Thread(target=open_url,args=[i])
    th.start()
print "end!!!"