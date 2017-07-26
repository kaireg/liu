#!/usr/bin/env python
# _*_ coding:utf-8 _*_


temp = "刘金恺"

temp_unicode = temp.decode('utf-8')

temp_gbk = temp_unicode.encode("gbk")

print(temp_gbk)

