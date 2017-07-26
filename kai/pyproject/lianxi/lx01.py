#!/usr/bin/env python
# liu coding:utf-8 liu

a = "aAsmr3idd4bgs7Dlsf9eAF"
print a.swapcase()

list_s = []
for x in a:
    if x.isdigit():
        list_s.append(x)
print list_s

a = a.lower()
for x in set(a):
    print dict([(x,a.count(x))])


