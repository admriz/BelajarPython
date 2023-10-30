
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = LEFT)

task1 = 0

redbutton = Button(frame, text = "Red", fg = "Red")
redbutton.pack(side = LEFT)
redbutton.event_add(a)
greenbutton = Button(frame, text = "Brown", fg = "Brown")
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ="Blue", fg = "blue")
bluebutton.pack(side = LEFT)
blackbutton = Button(bottomframe, text ="Black", fg = 'black')
blackbutton.pack( side = BOTTOM)

root.mainloop()