#!/usr/bin/env python
#导入numpy
import numpy as np

#首先创建一个长度为9的数组，然后转换成一个3x3的二维数组
n1 = np.arange(9).reshape(3,3)
print(n1)

#通过numpy创建随机数
a1 = np.random.randint(1,10,10)
print(a1)

#通过numpy将list转换为数组
list = [1,2,3,4,5,6,7,8,9]
l1 = np.array(list)
print(l1)

#numpy索引
i1 = np.arange(15).reshape(3,5)
print(i1)
print('-----------------------')
print(i1[1])
print(i1[1][1])
print(i1[1:3])