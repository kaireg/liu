#!/usr/bin/env python
#coding:utf-8

"""
定义一个列表的操作类：Listinfo

包括的方法:

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key()

list_info = Listinfo([44,222,111,333,454,'sss','333'])
"""

class listinfo(object):

    def __init__(self,list1):
        self.list1 = list1

    def add_key(self,keyname):
        self.list1.append(keyname)
        return self.list1

    def get_key(self,num):
        return self.list1[num]

    def update_list(self,list2):
        self.list1.extend(list2)
        return self.list1

    def del_key(self):
        return self.list1.pop()

list_info = listinfo([44,22,111,333,454,'sss','333'])

# print list_info.add_key("liu")
# print list_info.get_key(2)
# print list_info.update_list([2,3,4,5])
# print list_info.del_key()

"""
定义一个集合的操作类：Setinfo

包括的方法:

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)

"""

class setinfo(object):

    def __init__(self,setname):
        self.set1 = setname

    def add_setinfo(self,keyname):
        self.set1.add(keyname)
        return self.set1

    def get_interseckion(self,unioninfo):
        return self.set1 & unioninfo

    def get_union(self,unioninfo):
        return self.set1 | unioninfo

    def del_difference(self,unioninfo):
        return self.set1 - unioninfo

set_info = setinfo(set(['a','b','c','d',1,2,3,4]))

print set_info.add_setinfo(5)
print set_info.get_interseckion(set([1,2,3,4,5,6,7,8]))
print set_info.get_union(set([1,2,3,4,5,6,7,8]))
print set_info.del_difference(set([1,"k","b"]))

