#!/usr/bin/env python
#coding:utf-8

#类装饰器

class mydemo(object):

    def __init__(self,func):
        self.func =func
        print "这是__init__"

    def echo(self,name):
        print "你好,",name

    def __call__(self):
        self.func()
        print '这是__call__'

@mydemo
def demo():
    print '这是demo函数'

print "我是外面的"
demo()
print ' '
demo.echo('liu')


class MyApp():
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func

        return func_wrapper

    def call_method(self, name=None):
        func = self.func_map.get(name)
        if func is None:
            raise Exception("No function registered against - " + str(name))
        return func()


app = MyApp()


@app.register('1')
def main_page_func():
    return "This is the main page."


@app.register('2')
def next_page_func(name):
    return "This is the next page." + name


print app.call_method('1')
print next_page_func('hello')