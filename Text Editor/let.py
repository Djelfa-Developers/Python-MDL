from tkinter import *

root=Tk()
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New")
submenu.add_command(label="Open")
submenu.add_command(label="Close")

#just make separator between the labels
submenu.add_separator()
submenu.add_command(label="Sava")
submenu.add_command(label="Sava As")

#just make separator between the labels
submenu.add_command(label="Page Setup")
submenu.add_command(label="Quit")

root.mainloop()