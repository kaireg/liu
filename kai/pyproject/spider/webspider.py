#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


#以get方式请求斗鱼的分类页，声明编码
res = requests.get("https://www.douyu.com/directory")
res.encoding = "utf-8"

#获取请求到的网页内容，并解析
sam = res.text
soup = BeautifulSoup(sam,'html.parser')

#获取到网页中的所有直播分类
links = soup.select("#live-list-contentbox li")

#遍历出所有直播分类的title和url
titles = []
urls =[]
for link in links:
    title = link.select("p")[0].text
    url = "https://www.douyu.com" + link.select("a")[0]['href']
    titles.append(title)
    urls.append(url)



res = requests.get("https://www.douyu.com/directory/game/lol?page=2")
res.encoding = "utf-8"

sam = res.text
soup = BeautifulSoup(sam, 'html.parser')

# page1 = soup.select("script")
#
# page = str(page1[4].text)
#
# m = re.compile("[0-9]+")
# li = m.findall(page)

links = soup.select("#live-list-contentbox li")

try:
    for link in links:
        name = link.select("p span")[0].text
        num = link.select("a")[0]['href'][1:]
        renqi = link.select("p span")[1].text
        print(num,name,renqi)
except:
    pass
