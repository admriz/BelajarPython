from tkinter import *

layout = Tk()
S = Scale(layout, from_=0, to=50)
S.pack()
S = Scale(layout, from_=0, to=200, orient=HORIZONTAL)
S.pack()
mainloop()