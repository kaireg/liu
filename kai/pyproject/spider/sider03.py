#!/usr/bin/env python
# liu coding:utf-8 liu

import re         #正则模块
import urllib2    #urllib2模块
import urllib     #urlilnb模块
import time       #时间模块

x = 0
y = 0
sttime = time.clock()
list_num = []
for urlnum in range(171100,171138):     #30814
    strnum = str(urlnum)
    sturl = urllib.urlopen('http://www.neihan8.com/gif/' + strnum + '.html')
    rd_url = sturl.read()
    cod_url = sturl.getcode()

    if cod_url == 404 :
        x += 1
    else:
        list_num.append(strnum)
        print list_num[y]
        y += 1

print "本次总共爬取: %s 页面" %(x+y)
print "%s个页面不存在" % x
print "%s个页面可用" %y

endtime = time.clock()

print "程序花费时间为：%s 秒" %int(endtime - sttime)
