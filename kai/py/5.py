#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import time

i = 0
while i < 100:
	i = i +1
	j = i % 2
	if j == 0:
		print(i)
	time.sleep(0.1)
print("over")