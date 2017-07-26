#!/usr/bin/env python
#coding:utf-8

def max(a,b,c):
    if a>b:
        g=b
        b=a
        a=g
    if a>c:
        g=c
        c=a
        a=g
    if b>c:
        g=b
        b=c
        c=g
    print c
int_a = int(raw_input("a = " ))
int_b = int(raw_input("b = " ))
int_c = int(raw_input("c = " ))
max(int_a,int_b,int_c)
