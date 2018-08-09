from tkinter import *

root=Tk()
menu=Menu(root)
root.config(menu=menu)
first=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=first)
first.add_command(label="New")
first.add_command(label="Open")
first.add_command(label="Close")

#just make separator between the labels
first.add_separator()

first.add_command(label="Sava")
first.add_command(label="Sava As")

#just make separator between the labels
first.add_separator()

first.add_command(label="Page Setup")
first.add_command(label="Quit")

root.mainloop()
