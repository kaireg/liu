#!/usr/bin/env python
# liu coding:utf-8 liu


'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

def func(name):
    if isinstance(name,str):
        return name.capitalize()
    else:
        pass
# print func("lilei")
# print func("hanmeimei")
# print func("Hanmeimei")

'''
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"
'''
import string

def func_clbk(name,callback=None):
    if isinstance(name,str):
        if callback == None:
            return name.capitalize()
        else:
            return callback(name)
    else:
        pass
# print func("lilei")
# print func("LILEI",callback=string.lower)
# print func("lilei",callback=string.upper)

"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6

"""

def func_prt(*kargs):
    return kargs

# l = func(1,2,3,4,5)
# for i in l:
# 	print i,
# #输出 1 2 3 4 5
#
# print ''
#
# l = func(5,3,4,5,6)
# for i in l:
# 	print i,
# #输出 5 3 4 5 6


"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None
"""

def func_str(*kargs):
    list_i = []
    for i in kargs:
        if isinstance(i,str):
            list_i.append(i)
        else:
            pass
    if list_i == []:
        return None
    else:
        return list_i[0]
# print func_str(222,1111,'xixi','hahahah')
# print func_str(7,'name','dasere')
# print func_str(1,2,3,4)

"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"
"""

def func_name(name=None,**kargs):
    #列表推到式
    list_l = ["%s:%s" %(k,v) for k,v in kargs.items()]
    list_l.insert(0,name)
    return ','.join(list_l)
# print func_name("lilei")
# print func_name("lilei",years=4)
# print func_name("lilei",years=10,body_weight=20)

if __name__ ==  '__main__':
    print func("lilei")
    print func("hanmeimei")
    print func("Hanmeimei")
    print func_clbk("lilei")
    print func_clbk("LILEI",callback=string.lower)
    print func_clbk("lilei",callback=string.upper)
    l = func_prt(1,2,3,4,5)
    for i in l:
        print i,
    #输出 1 2 3 4 5

    print ''

    l = func_prt(5,3,4,5,6)
    for i in l:
        print i,
    #输出 5 3 4 5 6
    print ''
    print func_str(222,1111,'xixi','hahahah')
    print func_str(7,'name','dasere')
    print func_str(1,2,3,4)
    print func_name("lilei")
    print func_name("lilei",years=4)
    print func_name("lilei",years=10,body_weight=20)