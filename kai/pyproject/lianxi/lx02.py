#!/usr/bin/env python
# liu coding:utf-8 liu

a = "aAsmr3idd4bgs7Dlsf9eAF"

list_a = []
for x in a:
    if not x.isdigit():
        list_a.append(x)
print list_a
print ''.join(list_a)

