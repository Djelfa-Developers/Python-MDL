#!/usr/bin/python
# -*- coding: utf-8 -*-
# Said Gourida



import sys
from functions import about

if sys.version_info[0] == 3:  # Just checking your Python version to import Tkinter properly.
    from tkinter import *
    from tkinter import messagebox
else:
    from Tkinter import * # this from python 2 
    import tkMessageBox # this for python2 when you want to import messagebox 



def about(event=None):
    
    root_1 =Tk()
    #root.withdraw()
    root_1.title("Moino Abont")
    root_1.resizable(False,False)
    root_1.geometry("400x400+400+170")
    root_1.config(background="#593489")
    
    def close():
        root_1.destroy()   
        
    #myframe=Frame(root_1,bg="#303030",highlightbackground="white",highlightcolor="white",highlightthickness=1).place(height=170,width=320,x=41,y=100)
    product=Label(root_1,text="Product: ",fg="white",font="none 10 bold",bg="#593489").place(x=127,y=132)
    version=Label(root_1,text="Version: ",fg="white",font="none 10 bold",bg="#593489").place(x=130,y=151)
    release=Label(root_1,text="Release Date: ",fg="white",font="none 10 bold",bg="#593489").place(x=93,y=172)
    owner=Label(root_1,text="Owner: ",fg="white",font="none 10 bold",bg="#593489").place(x=137,y=191)
    os=Label(root_1,text="OS: ",fg="white",font="none 10 bold",bg="#593489").place(x=162,y=211)
    gui=Label(root_1,text="GUI Toolkit: ",fg="white",font="none 10 bold",bg="#593489").place(x=107,y=232)
    
    
    product1=Text(root_1,fg="white",font="none 10 bold",bg="#303030",borderwidth=0,height=0)
    product1.insert(0.0,"Moino Editor")
    product1.configure(state="disabled")
    product1.place(x=192,y=132,width=100)
    
    
    version1=Text(root_1,fg="white",font="none 10 bold",bg="#303030",borderwidth=0,height=0)
    version1.insert(0.0,"1.3.9")
    version1.configure(state="disabled")
    version1.place(x=192,y=152,width=100)
    
    release1=Text(root_1,fg="white",font="none 10 bold",bg="#303030",borderwidth=0,height=0,)
    release1.insert(0.0,"August 31 2018")
    release1.configure(state="disabled")
    release1.place(x=192,y=172,width=100)
    
    
    owner1=Text(root_1,fg="white",font="none 10 bold",bg="#303030",borderwidth=0,height=0)
    owner1.insert(0.0,"Gourida Said")
    owner1.configure(state="disabled")
    owner1.place(x=192,y=192,width=100)
    
    
    os1=Text(root_1,fg="white",font="none 9 bold",bg="#303030",borderwidth=0,height=0)
    os_ver=str(platform.platform() + platform.machine())
    os1.insert(0.0,os_ver)
    os1.configure(state="disabled")
    os1.place(x=192,y=212,width=167)
    
    gui1=Text(root_1,fg="white",font="none 10 bold",bg="#303030",borderwidth=0,height=0)
    gui1.insert(0.0,"Tkinter Version 8.6")
    gui1.configure(state="disabled")
    gui1.place(x=192,y=232,width=120)

    
    
    #style=ttk.Style()
    #style.configure("TButton")
    #lb=ttk.Button(root_1,text="Close",command=close).place(x=22,y=350,width=360)
    lb=Button(root_1,text="Close",width=40,foreground="white",borderwidth=2,bg="#F88C39",command=close).place(x=25,y=350)


    
#def New():


def open_file():
    global filename
    filename=tkFileDialog.askopenfilename(defaultextension=".txt",filetypes =[("All Files","*.*"),("Text Documents","*.txt")])
    if filename == "": # If no file chosen.
        filename = None # Absence of file.
    else:
        root.title(os.path.basename(filename) + " - pyPad") #
        #Returning the basename of 'file'
        e_text1.delete(1.0,END)
        fh = open(filename,"r")
        e_text1.insert(1.0,fh.read())
        fh.close()

#def close():
    
#def Setup():

def save():
    global filename
    try:
        f = open(filename, 'w')
        letter = e_text1.get(1.0, 'end')
        f.write(letter)
        f.close()
    except:
        save_as()
    
#------------------ main ----------------------
root=Tk()
root.title("Moino")
#root.resizable(True,True)
root.state('zoomed')


menu=Menu(root)
root.config(menu=menu)

#-------   some functions    ---------

def quit():
    if askokcancel("Quit", "Do you want to quit?"):
        # this for python2 
        # tkMessageBox.askokcancel("Quit","Do you want to quit?")
        root.destroy()
root.protocol(quit)


#-------   make first menu   ---------
first=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=first)
first.add_command(label="New",accelerator="Ctrl+N")
first.add_command(label="Open...,",accelerator="Ctrl+O")
first.add_command(label="Close",accelerator="Ctrl+W")

#make separator between the labels
first.add_separator()

first.add_command(label="Sava",accelerator="Ctrl+S")
first.add_command(label="Sava As...",accelerator="Ctrl+Shift+S")

#make separator between the labels
first.add_separator()

first.add_command(label="Page Setup...")
first.add_command(label="Quit",accelerator="Ctrl+Q",command=quit)

#-------   make second menu   ---------
second=Menu(menu,tearoff=0)

menu.add_cascade(label="Edit",menu=second)
second.add_command(label="Cut",accelerator="Ctrl+X")
second.add_command(label="Copy",accelerator="Ctrl+C")
second.add_command(label="Paste",accelerator="Ctrl+V")
second.add_command(label="Clear")

# make separator between the labels
second.add_separator()

# add new menu inside label select
select_menu=Menu(second,tearoff=0)
second.add_cascade(label="Select",menu=select_menu)
select_menu.add_command(label="Select All",accelerator="Ctrl+A")
select_menu.add_command(label="Select More",accelerator="Ctrl+Up")
select_menu.add_command(label="Select Less",accelerator="Ctrl+Down")

ser_rep=Menu(second,tearoff=0)
menu.add_cascade(label="Search and replace",menu=ser_rep)
ser_rep.add_command(label="Search",accelerator="Ctrl+F")
ser_rep.add_command(label="Replace",accelerator="Ctrl+H")
second.add_command(label="Goto Line...")

#-------   make third menu   ---------
third=Menu(menu,tearoff=0)
menu.add_cascade(label="Project",menu=third)
third.add_command(label="New Project...")
third.add_command(label="Open Project...")

select_menu1=Menu(third,tearoff=0)
third.add_cascade(label="Recent",menu=select_menu1)
select_menu1.add_command(label="Default Project")

third.add_command(label="Add New File")
third.add_command(label="Add Existing File")

# make separator 
third.add_separator()
third.add_command(label="Show Current File in Project Tool")
# make separator 
third.add_separator()
third.add_command(label="Project Properties...")

#-------   make last menu   ---------
last=Menu(menu,tearoff=0)
menu.add_cascade(label="Help",menu=last)
last.add_command(label="Moino Manual")
last.add_command(label="Tutorial")

# make separator 
last.add_separator()
last.add_command(label="Python Manual (HTML)...")
last.add_command(label="Python Website...")
last.add_command(label="Python Interface to Tcl/Tk")
last.add_command(label="Python Turtle Graphics")
# make separator 
last.add_separator()
last.add_command(label="Check for Updates...")
last.add_command(label="About...",command=about)


root.mainloop()
