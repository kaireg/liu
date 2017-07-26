#!/usr/bin/env python

import requests
res = requests.get('http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml')
res.encoding = 'gb2312'
# print(res.text)

from bs4 import BeautifulSoup
sam = res.text
soup = BeautifulSoup(sam,'html.parser')
# print(soup.text)

blink = soup.select('li')
i = 1
for link in blink:
    time = link.select('span')[0].text
    title = link.select('a')[0].text
    url = link.select('a')[0]['href']
    print(i ,time,title,url)
    i += 1

body = requests.get('http://news.sina.com.cn/c/nd/2016-12-14/doc-ifxytkcf7612191.shtml')
body.encoding = 'utf-8'

bodysam = body.text
bodysoup = BeautifulSoup(bodysam,'html.parser')
bodytime = bodysoup.select('.time-source')[0].contents[0]
bodyyuan = bodysoup.select('.time-source span a')[0].text
bodytielt = bodysoup.select('#artibodyTitle')[0].text
bodybody = bodysoup.select('#artibody p')[0:4]
print(bodytime,bodyyuan,bodytielt)
# print(bodytime , bodyyuan , bodytielt)
