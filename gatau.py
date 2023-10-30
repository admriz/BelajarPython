from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, "Python")
Lb.insert(2, "HTML")
Lb.insert(3, "C++")
Lb.insert(4, "Rubby")

Lb.pack()
top.mainloop()
