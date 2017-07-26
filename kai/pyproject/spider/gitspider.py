#!/usr/bin/env python
#coding:utf-8

import requests
from bs4 import BeautifulSoup


for i in range(1,11):
    i = str(i)
    url = 'http://www.cilibaike.org/word/%E9%87%91%E8%89%BA%E8%B4%9E_' + i + '.html'
    req = requests.get(url)
    req.encoding = "utf-8"

    sam = req.text
    soup = BeautifulSoup(sam,'html.parser')

    alink = soup.select("#fe_text")

    text = alink[0].text

    print(text)