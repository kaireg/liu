#!/usr/bin/env python
#coding:utf-8

import re
import requests
from bs4 import BeautifulSoup


class douyu(object):

    def __init__(self):
        pass

    def url(self,url):
        res = requests.get(url)
        res.encoding = "utf-8"

        sam = res.text
        soup = BeautifulSoup(sam, 'html.parser')

        return soup

    def list(self,soup):
        titles = []
        urls = []
        links = soup.select("#live-list-contentbox li")
        for link in links:
            title = link.select("p")[0].text
            url = "https://www.douyu.com" + link.select("a")[0]['href']
            titles.append(title)
            urls.append(url)
        return titles, urls

    def page(self,soup):
        page1 = soup.select("script")
        page2 = str(page1[4].text)

        m = re.compile("[0-9]+")
        page1 = m.findall(page2)[1]
        page = int(page1)
        return page

    def bady(self,soup):
        names = []
        nums = []
        renqis = []
        links = soup.select("#live-list-contentbox li")

        for link in links:
            name = link.select("p span")[0].text
            num = link.select("a")[0]['href'][1:]
            renqi = link.select("p span")[1].text
            names.append(name)
            nums.append(num)
            renqis.append(renqi)
        return names, nums, renqis

    def end(self):
        pass


d = douyu()
url = 'https://www.douyu.com/directory'
text = d.url(url)
print(d.list(text))