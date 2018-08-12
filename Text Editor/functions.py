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



def about():
    root_1 =Tk()
    #root.withdraw()
    root_1.title("Moino Abont")
    root_1.resizable(False,False)
    root_1.geometry("400x400+400+170")
    root_1.config(background="#593489")
    
    def close():
        root_1.destroy()    
    
    #style=ttk.Style()
    #style.configure("TButton")
    #lb=ttk.Button(root_1,text="Close",command=close).place(x=22,y=350,width=360)
    lb=Button(root_1,text="Close",width=50,foreground="white",borderwidth=2,width=50,bg="#F88C39",command=close).place(x=22,y=350)

