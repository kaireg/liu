#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import time

i = 0 
while i < 10 :
	i = i + 1
	if i == 7 :
		continue
	print(i)
	time.sleep(0.2)