#!/usr/bin/env python

from tkinter import Tk
from time import sleep
import win32com.client as win32


def excel():
    app = 'excel'
    xl = win32.gencache.EnsureDispatch('%s.Application' % app)
    ss = xl.Workbooxks.add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(1)

    sh.Cells(1,1).Value = 'Python-to-%s Demo' % app
    sleep(1)
    for i in range(3,8):
        sh.Cells(i,1).Value = 'Line %d' % i
        sleep()
    sh.Cells(i+2,1).Value = "Th-th-th-that`s all folks"

    ss.Close(False)
    xl.Application.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    excel()