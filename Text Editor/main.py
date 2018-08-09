from tkinter import *

root=Tk()
menu=Menu(root)
root.config(menu=menu)

#-------   make first menu   ---------
first=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=first)
first.add_command(label="New")
first.add_command(label="Open")
first.add_command(label="Close")

#make separator between the labels
first.add_separator()

first.add_command(label="Sava")
first.add_command(label="Sava As")

#make separator between the labels
first.add_separator()

first.add_command(label="Page Setup")
first.add_command(label="Quit")

#-------   make second menu   ---------
second=Menu(menu,tearoff=0)

menu.add_cascade(label="Edit",menu=second)
second.add_command(label="Cut")
second.add_command(label="Copy")
second.add_command(label="Paste")
second.add_command(label="clear")

# make separator between the labels
second.add_separator()

second.add_command(label="Select")
second.add_command(label="Search and replace")
second.add_command(label="Goto Line")

root.mainloop()
