#!/usr/bin/env python
# liu coding:utf-8 liu

list_a = [11,22,24,29,30,32]
print list_a
list_a.append(28)
print list_a

list_a.insert(4,57)
print list_a

list_a[0] = 6
print list_a

del list_a[-2]
print list_a

#list_a.pop(-2)
#print list_a

list_a.sort()
print list_a

list_b = [1,2,3,4,5]

#list_c = [6,7,8]
#list_b += list_c
#print list_b

list_b.extend([6,7,8])
print list_b

print list_b[-4:-6:-1]

list_bb = []
list_bb.append(list_b.pop(-4))
list_bb.append(list_b.pop(-4))
print list_bb

print  2 in list_b

list_c = [23,45,22,44,25,66,78]
