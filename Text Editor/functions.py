#!/usr/bin/python
# -*- coding: utf-8 -*-
# Said Gourida


import sys

if sys.version_info[0] == 3:  # Just checking your Python version to import Tkinter properly.
    from tkinter import *
    from tkinter import messagebox
else:
    from Tkinter import * # this for python 2 
    import tkMessageBox # this for python2.x when you want to import messagebox

    
    
def quit():
    root.destroy()

