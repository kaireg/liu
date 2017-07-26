#!/usr/bin/env python
#coding:utf-8


#非波拉契数列
def fiber(num):
    x,y =1,1
    while x < num:
        yield x
        x,y = y,x+y

# for i in fiber(388):
#     print i

#素数，只能被自己和1整除的数，称之为素数
def su(num):
    if num <= 1:
        return False
    elif num ==2:
        return True
    else:
        for i in xrange(2,num):
            if num %i == 0:
                return False
        return True

def get(max):
    su_max = []
    for x in xrange(1,max+1):
        if su(x):
            su_max.append(x)
    return su_max

#列表推导式
def get1(max1):
    return [x for x in xrange(1,max1+1) if su(x)]


# print get(101)
# print get1(101)

#10000以后的100个素数
def get_num():
    i = 0
    i_list = []
    for x in range(10000,1000000):
        if su(x):
            i = i+1
            i_list.append(x)
        if i == 101:
            return i_list
print get_num()
