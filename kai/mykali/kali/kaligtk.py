#!/usr/bin/env python
#coding:utf-8

import gtk
import pygtk

def destroy(widget,data=None):
    gtk.main_quit()

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("destroy",destroy)
window.show()

gtk.main()



