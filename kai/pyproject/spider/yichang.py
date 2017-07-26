#!/usr/bin/env python
#coding:utf-8

#异常捕获

try:
    #可能会抛出异常的代码块
    pass
except:
    #try中如果抛出了异常，该执行的内容
    pass
else:
    #try中没有抛出异常该执行的内容
    pass
finally:
    #不管try中有没有抛出异常都要执行的内容
    pass


#断言,只断言绝对不可能出现的错误,开发测试时期常用的一种检定代码的方式
# assert 表达式 ，出错后抛出的message