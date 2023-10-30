from tkinter import *
layout = Tk()
v = IntVar()

Radiobutton(layout, text="Male", variable= v, value=1).pack(anchor=W)
Radiobutton(layout, text="Female", variable=v, value=2).pack(anchor=W)
mainloop()