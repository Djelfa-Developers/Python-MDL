#!/usr/bin/python
# -*- coding: utf-8 -*-
# Said Gourida

import sys

if sys.version_info[0] == 3:  # Just checking your Python version to import Tkinter properly.
    from tkinter import *
else:
    from Tkinter import *

    
    
def quit():
    root.destroy()

