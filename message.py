from tkinter import *

def pesan():
    main = Tk()
    ourMessage = "Tulis Pesan Disini"
    messageVar = Message(main, text=ourMessage)
    messageVar.config(bg='Lightpink')
    messageVar.pack()
    mainloop()