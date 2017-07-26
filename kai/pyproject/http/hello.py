#!/usr/bin/env python
# coding:utf-8

#web应用程序的wsgi处理函数。

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','Text/html')])
    return '<h1>%s,hello,world!</h1>'%(environ['PATH_INFO'][1:] or 'web')
