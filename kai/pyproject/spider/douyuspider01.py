#!/usr/bin/env python
#coding:utf-8

import re
import requests
from bs4 import BeautifulSoup
import datetime

def get_url(url):
    res = requests.get(url)
    res.encoding = "utf-8"

    sam = res.text
    soup = BeautifulSoup(sam, 'html.parser')

    return soup

titles = []
urls = []

def get_list(soup):
    links = soup.select("#live-list-contentbox li")
    for link in links:
        title = link.select("p")[0].text
        url = "https://www.douyu.com" + link.select("a")[0]['href']
        titles.append(title)
        urls.append(url)
    return titles,urls

def get_page(soup):

    page1 = soup.select("script")
    page2 = str(page1[4].text)
    try:
        m = re.compile("[0-9]+")
        page1 = m.findall(page2)[1]
        page = int(page1)
    except:
        return 1
    return page


def get_bady(soup):
    names = []
    nums = []
    renqis = []
    try:
        links = soup.select("#live-list-contentbox li")
        for link in links:
            name = link.select("p span")[0].text
            num = link.select("a")[0]['href'][1:]
            renqi = link.select("p span")[1].text
            names.append(name)
            nums.append(num)
            renqis.append(renqi)
    except:
        return names,nums,renqis
    return names,nums,renqis

if __name__ == '__main__':
    print(datetime.datetime.now())
    ren = []
    url = 'https://www.douyu.com/directory'
    soup = get_url(url)
    list = get_list(soup)[1]
    for i in list:
        su = get_url(i)
        pg = get_page(su)
        if pg > 1 :
            for x in range(1,pg+1):
                x = str(x)
                urlx = i + "?page=" + x
                soup_list = get_url(urlx)
                bodyx = get_bady(soup_list)
                ren.extend(bodyx[2])
        else:
            soup1 = get_url(i)
            body1 = get_bady(soup1)
            ren.extend(body1[2])
    zong = 0
    for n in ren:
        if "万" in n:
            zh = int(float(n[:-1]) * 10000)
            zong += zh
        elif n == 0:
            pass
        else:
            zong += int(n)
    print(zong)
    print(datetime.datetime.now())
