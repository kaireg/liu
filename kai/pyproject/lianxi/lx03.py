#!/usr/bin/env python
# QAQ coding:utf-8 QAQ

import string

a = "12345678987654321"
print a

#replcae 是以字符串的方式全部替换
print a.replace('123','liu')

#maketrans translate 是逐个替换
b = string.maketrans('123','liu')
print a.translate(b)

c = string.maketrans('','')
print a.translate(c,'123')


#对文件进行操作
g = open('a.txt','w')
g.write('liu')
g.close()