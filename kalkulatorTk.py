from tkinter import *

layar = Tk()
layar.title("Aplikasi Kalkulator")
layar.geometry("400x200")

label = Label(layar, text="Insert Number :", anchor="e")
label.grid(column=0, row=0)

num1 = Entry(layar, width=10)
num1.grid(column=1, row=0)

label2 = Label(layar, text="Insert Number :",anchor="e")
label2.grid(column=0,row=1)

num2 = Entry(layar, width=10)
num2.grid(column=1, row=1)

label3 = Label(layar, text="Result :",anchor="e",width=25)
label3.grid(column=0,row=2)

result = Label(layar, text="0", anchor="w",width=10)
result.grid(column=1, row=2)

def plus():
    result.configure(text=int(num1.get())+int(num2.get()))

btn = Button(layar, text="Plus", command=plus)
btn.grid(column=0, row=3)

def kali():
    result.configure(text=int(num1.get())*int(num2.get()))

btn = Button(layar, text="Kali", command=kali)
btn.grid(column=0, row=4)

def minus():
    result.configure(text=int(num1.get())-int(num2.get()))

btn = Button(layar, text="Minus", command=minus)
btn.grid(column=0, row=5)

def bagi():
    result.configure(text=int(num1.get())/int(num2.get()))

btn = Button(layar, text="Bagi", command=bagi)
btn.grid(column=0, row=6)


mainloop()