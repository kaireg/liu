#!/usr/bin/env python

import requests  #导入requests模块
from bs4 import BeautifulSoup      #从bs4模块导入BeautifulSoup



keyword = "8187"
res = requests.get("http://search.jd.com/Search?keyword=" + keyword + "&enc=utf-8")
res.encoding = "utf-8"

sam = res.text
soup = BeautifulSoup(sam,'html.parser')

alink = soup.select('ul .gl-item')
for link in alink:
    imgurl = link.select('img')[0]
    title = link.select('em')[1].text
    price = link.select('.p-price i')[0].text
    url = link.select('a')[0]['href'][2:]
print(price,title,url,imgurl)


