#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#list = []
#tuple = ()
#dic = {}

#字典的每一个元素，键值对
usr_info = {
    "name": "liu",
    "age": 22,
    "gender": 'M'
}

#索引
print usr_info['age']

#循环 默认获取key
for i in usr_info:
    print i

#获取所有的key
print usr_info.keys()

#获取所有的值
print usr_info.values()

#获取所有的键值对
print usr_info.items()

for x,y in usr_info.items():
    print x
    print y


#清空字典
#usr_info.clear()
#print usr_info

#get 根据key获取值，如果不存在，可以指定一个默认值None
val = usr_info.get('age')
print val
zhi = usr_info.get('kai')
print zhi

#通过索引取值时，不存在将报错
#print usr_info['abc']

# has_key 检查字典中指定的key是否存在 3.X已经移除 用in代替
abc = "age" in usr_info.keys()
print abc

print usr_info.has_key('age')

#update
dict_info = {
    "bb": "jin",
    "cc": "kai"
}
print usr_info.update(dict_info)

#pop
print dict_info

print dict_info.pop('cc')

dict_info.popitem()
print dict_info