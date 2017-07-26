#!/usr/bin/env python

class myfoo():
    def __init__(self,name):
        self.name = name

    def name(self):
        print("liu"+ self.name)

class foo(myfoo):
    pass

bs = myfoo('liu')
bs.name()

