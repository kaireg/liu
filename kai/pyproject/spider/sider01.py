#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import string,urllib2

def baidu_tieba(url,begin,end):
    for i in range(begin,end+1):
        sName = string.zfill(i,5) + '.html'
        print '正在下载' + str(i) +'个网页 ，并将其存储为' + sName + '......'
        f = open(sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

bdurl = str("http://tieba.baidu.com/p/")
begin = int("1")
end = int("10")

baidu_tieba(bdurl,begin,end)
