#!/usr/bin/env python
# QAQ coding:utf-8 QAQ

def get_num(list_num):
    #创建空的列表，承载参数中的偶数
    list_a = []
    #判断输入的参数是否为list
    if not isinstance(list_num,list):
        return "参数不对，请输入列表参数"
    else:
        #for遍历列表中的每个值是否为整型
        for i in list_num:
            if not isinstance(i,int):
                return "你输入的参数不正确，请输入整数参数"
            else:
                #判断参数是否为偶数，为偶数就添加到list_a中
                if i%2 == 0:
                    list_a.append(i)
    return list_a
print get_num([1,2,3,4,5,6,7,8,10])
print get_num([1,2,3,4,5,6,7,8,'jkl'])
print get_num('dsf')

import urllib

def get_page(url):
    url_page = urllib.urlopen(url)
    url_nr = url_page.getcode()
    if url_nr == 404:
       return "页面不存在，请检查你输入的url"
    else:
        return url_page.read()
print get_page('http://www.neihan8.com/gif/000.php')

