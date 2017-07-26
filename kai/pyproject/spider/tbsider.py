#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

res = requests.get('https://shopsearch.taobao.com/search?app=shopsearch&q=%E8%82%89%E7%B3%95&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20161219&ie=utf8')
res.encoding = 'utf-8'
print(res.text)