import message
from tkinter import *

root = Tk()
menu = Menu(root)

root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label = "Name")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label = "help", menu = helpmenu)
helpmenu.add_command(label="ABOUT")

View = Menu(menu)
menu.add_cascade(label = "View", menu = View)
View.add_command(label="Tool Window")
View.add_command(label="Appearance")
View.add_separator()
View.add_command(label="Quick Definition")
View.add_command(label="Quick Type Definition")
View.add_command(label="Parameter Info")
View.add_command(label="Type Info")
View.add_command(label="Context Info")
View.add_command(label="List Info")
View.add_separator()

mainloop()
