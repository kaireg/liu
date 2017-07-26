#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

res = requests.get('http://money.163.com/special/pinglun/')
res.encoding = "gbk"

sam = res.text
soup = BeautifulSoup(sam,'html.parser')

alink = soup.select(".item_top")

# print(alink)

i = 1
for link in alink:
    title = link.select('h2')[0].text
    time = link.select(".time")[0].text
    url = link.select('h2 a')[0]['href']
    print(i,title,time,url)
    i += 1
