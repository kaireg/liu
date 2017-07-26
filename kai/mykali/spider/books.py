#!/usr/bin/env python
#coding:utf-8


import requests
from bs4 import BeautifulSoup

def get_url(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    htext = html.text
    return htext

def bs_htext(soup):
    bklist = []
    soup = BeautifulSoup(soup, "html.parser")
    lis = soup.select('#subject_list ul li')
    for i in lis:
        booklist = i.select('.pub')[0].text.strip()
        bklist.append(booklist)
    return bklist

def bk_list(bklist):
    pass

sop = get_url('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=0&type=T')
bklt = bs_htext(sop)
bk_list(bklt)