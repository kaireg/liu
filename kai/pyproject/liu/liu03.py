#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# list
#列表
name = "liu"
age = 21
name_list = ["liu","jin","kai"]
age_list = [15,20,40]
print name,age,name_list,age_list

#往列表最后追加元素
name_list.append('ljk')
print name_list

name_list.append('ljk')
name_list.append('ljk')
print name_list

#计算列表里有多少个这个元素
print name_list.count('ljk')

#往列表里批量添加元素
name_list.extend(age_list)
print name_list

#计算列表里某一个元素所在的位置
print name_list.index('kai')

#往列表指定位置添加元素
name_list.insert(1,'biubiubiu')
print name_list

#移除掉列表里的某个元素并赋给a1 默认为-1
a1 = name_list.pop(1)
print name_list
print a1

#移除列表里的某个元素,只移除左边第一个元素
name_list.remove('ljk')
print name_list

#翻转列表中的元素
name_list.reverse()
print name_list

#将列表排序
name_list.sort()
print name_list

#删除列表里指定的元素
del name_list[0:3]
print name_list

