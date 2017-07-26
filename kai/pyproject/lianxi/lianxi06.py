#!/usr/bin/env python
#liu coding:utf-8 liu

"""
 二：用异常方法，处理下面需求：

 info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm'.

...]任意多的网址

 2.1 定义一个方法get_page(listindex) listindex为下标的索引，

类型为整数。 函数调用：任意输入一个整数，返回列表下标对应UR

L的内容，用try except 分别捕获列表下标越界和url 404 not found

的情况。

 2.2 用logging模块把404的url，记录到当前目录下的urlog.txt。

urlog.txt的格式为：2013-04-05 15:50:03,625 ERROR

http://wwwx.com 404 not foud

"""
import urllib
import logging

logger = logging.getLogger()

hdlr = logging.FileHandler('log.txt')

formatter = logging.Formatter('%(asctime)s %(levelname)s%(filename)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr)

logger.setLevel(logging.NOTSET)

def get_page(listindex):
    info = ['http://www.163.com', 'http://www.baidu.com',
            'http://www.abc.com', 'http://safdsafds']
    try:
       urlpage =  info[listindex]
    except:
        return "输入的参数无效，超出列表索引"
    try:
        a = urllib.urlopen(urlpage)
    except:
            return "url 404 not gound "
            logger.error(urlpage)
    else:
        return a.read()

print get_page(3)