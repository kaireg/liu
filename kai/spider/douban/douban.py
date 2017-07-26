#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re

url = 'https://book.douban.com/tag/?icn=index-nav'
req = requests.get(url)
req.encoding = "utf-8"

sam = req.text
soup = BeautifulSoup(sam,'html.parser')

links = soup.select('.article tr')

list =[]
for i in links:
    x = i.text
    y = re.compile('[0-9]+')
    z = y.findall(x)
    list.extend(z)

num = 0
for b in list:
    b = int(b)
    num = num + b
print(num)