#!/usr/bin/env python
# liu coding:utf-8 liu

import re
import urllib



wangye = urllib.urlopen('http://www.neihan8.com/gif/171134.html')

neirong = wangye.read().decode('utf-8')

RegularExpression = 'href="(.*)"'

Valuable = re.findall(RegularExpression,neirong)

print Valuable


#<a rel="nofollow" href="(.*)"  title="下翻页">下一页→</a></div>




