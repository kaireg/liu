#!/usr/bin/env python
# _*_ coding:utf-8 _*_


i = 0 
k = 0
while i < 100:
	i = i + 1
	j = i % 2
	if j == 0:
		k = k - i
	else:
		k = k + i
print(k)