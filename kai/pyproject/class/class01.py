#!/usr/bin/env python
#coding:utf-8

class test(object):

#在class实例化时，引入一些必要的参数
    def __init__(self,var1):
        self.var = var1


#get称之为test对象的方法
    def get(self,a=None):
        return self.var

#这里是将class实例化
t = test("hello,world")

"""
一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int


写好类以后，可以定义2个同学测试下:

zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100

lq = student('liqiang',23,[82,60,99])

返回结果：
liqiang
23
99
"""

class stu(object):

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.course)

zm = stu('zhangming',20,[69,88,100])
lq = stu('liqiang',23,[82,60,99])
# print zm.get_name()
# print zm.get_age()
# print zm.get_course()
# print lq.get_name()
# print lq.get_age()
# print lq.get_course()


"""
二：定义一个字典类：dictclass。完成下面的功能：

dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)

2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})

"""

class dictclass(object):

    def __init__(self,dict_name):
        self.dict_name = dict_name

    def del_dict(self,key):
        del self.dict_name[key]
        return self.dict_name

    def get_dict(self,key):
        return self.dict_name.get(key,"not found")

    def get_key(self):
        return self.dict_name.keys()

    def update_dict(self,dict_update):
        self.dict_name.update(dict_update)
        return self.dict_name.values()

dict = dictclass({
    "name": "liu",
    "age" : 21,
    "gender": "M",
    "bool" : "Ture"
})

print (dict.get_dict("hgj"))
print (dict.get_key())
print (dict.del_dict("age"))
print (dict.update_dict({"hello":"world","father":"kai"}))