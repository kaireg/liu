#!/usr/bin/env python
# _*_ coding:utf-8 _*_

for x in xrange(1,10):
	for y in xrange(x,10):
		print("%d*%d=%2d" % (x,y,x*y)),
	print(" ")