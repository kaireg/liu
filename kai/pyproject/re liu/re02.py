#!/usr/bin/env python




"""
1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'

用正则模块提取出网址："http://www.baidu.com"和

链接文本:"baidu"
"""

import re

x = ["1万","1.4万","432万","123","20.2万","0","4322"]
wan = 0

for i in x:
    if "万" in i:
        y = int(float(i[:-1]) * 10000)
        wan += y
    else:
       wan += int(i)
print(wan)
