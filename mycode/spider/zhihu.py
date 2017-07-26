import re
import requests
from bs4 import BeautifulSoup

def get_url(url):
    res = requests.get(url)                     #传入url地址
    res.encoding = "utf-8"                      #设置网页编码格式
    sam = res.text                              #获取网页内网
    soup = BeautifulSoup(sam,'html.parser')     #将网页内容解析
    alink = soup.select('body .reader')                #获取该文档中需要的部分
    return alink

def get_pages(alink):      #获取该文档页数
    for link in alink:
        page = link.select('.info')[0].text
    page = str(page)
    page = re.findall(r'(\w*[0-9]+)\w*',page)
    pages = page[-1][1:]
    return pages

txt = []
def get_txt(alink):       #获取该文档内容
    for link in alink:
        text = link.select('.txt')
        for t in text:
            txt.append(t.text)

if __name__ == '__main__':
    url = input("请你输入百度文库的地址:")
    alink = get_url(url)
    pages = int(get_pages(alink))
    urls = url[:-3]
    for i in range(1,pages+1):
        urlx = urls + 'pn=' + str(i) + '&pu='
        link_page = get_url(urlx)
        get_txt(link_page)
    print(txt)




