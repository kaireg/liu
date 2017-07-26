#!/usr/bin/env python
# liu coding:utf-8 liu


#lambda的用法
a = [1,2,3,4,5,6]
b = filter(lambda x: x != 5,a)
print b

c = []
for i in a:
    if i != 5:
        c.append(i)
print c