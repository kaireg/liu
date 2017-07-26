
import re
import requests
from bs4 import BeautifulSoup

def get_url(url):
    res = requests.get(url)
    res.encoding = "utf-8"

    sam = res.text
    soup = BeautifulSoup(sam, 'html.parser')

    return soup

body_list = []
def get_list(soup):
    links = soup.select("p")
    for link in links:
        body = link.select("#txt")[0].text
        body_list.append(body)
    return body_list

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

if __name__ == '__main__':
    url = 'https://wapwenku.baidu.com/view/6a290feeccbff121dc36835f.html?pn=8&pu='
    text = get_url(url)
    get_list(text)
    print(body_list)