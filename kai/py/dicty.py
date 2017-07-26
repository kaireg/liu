#!/usr/bin/env python

li = [11,22,33,44,55,66,77,88,99]

dic = {
	"k1":[],
	"k2":[],
}

for x in li:
	if x <= 66:
		dic['k1'].append(x)
	else:
		dic['k2'].append(x)

print(dic)