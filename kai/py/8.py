#!/usr/bin/env python
# _*_ coding:utf-8 _*_


for i in xrange(1,5):
	for j in xrange(1,5):
		for k in xrange(1,5):
			if ( i != j ) and ( j != k ) and ( i != k ):
				print i,j,k
