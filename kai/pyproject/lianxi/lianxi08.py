#!/usr/bin/env python
#coding:utf-8

#yield
# 包含yield函数，则是一个可迭代对象
# 利用next（）取下一个yield的值
# 利用send（）向yield传递参数
# 不管是next，send都会到下一个yield的值


def yed():
    i = 0
    a = 4
    while i < a:
        x = yield i
        i += 1

for i in yed():
    print i

print "\n"

print yed()

print "\n"

y = yed()
print y.next()
print y.next()
print y.next()
print y.next()

print "\n"

print range(0,6)
print xrange(0,6)

print "\n"
def func():
    x = yield "这是第一个yield！"
    print ' 这是输出  %s' %x
    x = yield "这是第二个yield！"
    print ' 这是输出   %s' %x
    x = yield "这是第三个yield"
f = func()
print f.next()
print f.next()
print f.next()

print "\n"

def func1():
    x = yield "这是第一个yield！"
    print ' 这是输出  %s' %x
    x = yield "这是第二个yield！"
    print ' 这是输出   %s' %x
    x = yield "这是第三个yield"
f = func1()
print f.next()
print f.send("this is one")
print f.send("this is two")

print "\n"



#非波拉契数列
def fiber(num):
    x,y =1,1
    while x < num:
        yield x
        x,y = y,x+y

for i in fiber(388):
    print i