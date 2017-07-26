#!/usr/bin/env python
#coding:utf-8

import collections

#计数器，计算每个元素出现的次数
obj = collections.Counter('fgfdsgfdsfddagfdafdsagfdhfggdsafdsahgfdfdsa')

#获取字典中次数多的前n位的值，返回一个list
ret = obj.most_common(n=4)

#update 没有则增加  有就加一
#subtract 删除元素

print(obj)

print(ret)

#获取Counter中的所有的元素,原生值
for key in obj.elements():
    print(key)

#获取Counter中的key，vleas
for k,v in obj.items():
    print(k,v)