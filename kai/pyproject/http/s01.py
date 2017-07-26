#!/usr/bin/env python
#coding:utf-8

#socket
#tcp/ip
#udp

import socket
#这里定义一个socket，需要有两个参数，第一个参数是哪种模式，
#1.基于ip的通信  AF_INET    2.基于本机的通信只能进行单一的unix系统通信  AF_UNIX
#第二个参数  是选择哪种模式     SOCK_STREAM tcp/ip      SOCK_DGREAM udp
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s = socket.socket(socket.AF_INET,socket.SOCK_DGREAM)
#绑定ip和端口
s.bind(('127.0.0.1',8125))
#监听参数是同时允许处理的请求的次数
s.listen(8)
while 1:
        connection,address = s.accept()
        buf = connection.recv(1024)
        connection.send(buf)
s.close()
