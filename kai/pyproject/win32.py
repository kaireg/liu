#!/usr/bin/env python
#coding:utf-8

import win32api
import win32con
import time
import os

'''
除了使用os模块中的os.system()函数以外，还可以使用win32api模块中的ShellExecute()函数。其函数如下所示。
ShellExecute(hwnd, op , file , params , dir , bShow )
其参数含义如下所示。
·     hwnd：父窗口的句柄，如果没有父窗口，则为0。
·     op：要进行的操作，为“open”、“print”或者为空。
·     file：要运行的程序，或者打开的脚本。
·     params：要向程序传递的参数，如果打开的为文件，则为空。
·     dir：程序初始化的目录。
·     bShow：是否显示窗口。
'''


# win32api.MessageBox(win32con.NULL,'hello','world',win32con.MB_OK)

# win32api.ShellExecute(0, 'open', 'https://www.douyu.com/', '','',1)

# time.sleep(3)

# d = os.system('for /r d: %i in (*cloudmusic.exe*) do @echo %i')


win32api.ShellExecute(0,'open','D:\Program Files (x86)\music\cloudmusic.exe' ,'','',1)

