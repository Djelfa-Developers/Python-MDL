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
        
        
    myframe=Frame(root_1,bg="#303030",highlightbackground="white",highlightcolor="white",highlightthickness=1).place(height=170,width=320,x=41,y=100)
    product=Label(myframe,text="Product: ",fg="white",font="none 10 bold",bg="#303030").place(x=131,y=130)
    version=Label(myframe,text="Version: ",fg="white",font="none 10 bold",bg="#303030").place(x=132,y=150)
    release=Label(myframe,text="Release Date: ",fg="white",font="none 10 bold",bg="#303030").place(x=96,y=170)
    owner=Label(myframe,text="Owner: ",fg="white",font="none 10 bold",bg="#303030").place(x=138,y=190)
    os=Label(myframe,text="OS: ",fg="white",font="none 10 bold",bg="#303030").place(x=161,y=210)
    gui=Label(myframe,text="GUI Toolkit: ",fg="white",font="none 10 bold",bg="#303030").place(x=110,y=230)
    
    #style=ttk.Style()
    #style.configure("TButton")
    #lb=ttk.Button(root_1,text="Close",command=close).place(x=22,y=350,width=360)
    lb=Button(root_1,text="Close",width=50,foreground="white",borderwidth=2,bg="#F88C39",command=close).place(x=22,y=350)
   



   
    
    

