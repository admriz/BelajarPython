import sys
import tkinter
from packaging import version
from PIL import ImageTk, Image
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('green')

app=customtkinter.CTk()
app.geometry('600x440')
app.title('Login')
def fungsilogin():
    usr = "admin"
    pw = "adam"
    usrbnr = entry1.get()
    pwbnr = entry2.get()

    if usr == usrbnr and pw == pwbnr:
        fungsi()

    elif pw == entry2 or usr == usrbnr:
        gagal("Password")
    elif usr == entry1 or pw == pwbnr:
        gagal("Username")
    else:
        gagal("Login")

def gagal(wrong):
    wow = customtkinter.CTkLabel(master=frame, text="                                                                                             ",text_color="red", font=("Century Gothic", 10))
    wow.place(x=39, y=325)
    l3 = customtkinter.CTkLabel(master=frame, text=f"{wrong} Invalid", text_color="red", font=("Century Gothic", 12))
    l3.place(x=118, y=325)

def available(name):
    wow = customtkinter.CTkLabel(master=frame,text="                                                                                             ",text_color="red", font=("Century Gothic", 10))
    wow.place(x=39, y=325)
    wow = customtkinter.CTkLabel(master=frame, text=f"Sorry for the moment that {name} is not available.", text_color="red", font=("Century Gothic", 10))
    wow.place(x=39, y=325)


def fungsi():
    app.destroy()
    w=customtkinter.CTk()
    w.geometry('1280x720')
    w.title('Main Screen!')
    l1=customtkinter.CTkLabel(master=w, text="Welcome!", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    w.mainloop()



img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Login", font=("Century Gothic",25))
l2.place(x=130,y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
entry2.place(x=50, y=165)

l3=customtkinter.CTkLabel(master=frame, text="Forget Password?", font=("Century Gothic",12))
l3.place(x=155,y=195)

btn = customtkinter.CTkButton(master=frame, width=220, text="Login", corner_radius=6, command=fungsilogin)
btn.place(x=50, y=240)

img2 = customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20, 20)))
img3 = customtkinter.CTkImage(Image.open("124010.png").resize((20, 20)))

btn1 = customtkinter.CTkButton(master=frame, width=100, image=img2, text="Google", height=20, corner_radius=6, compound="left", text_color = "black", fg_color= "white", command=available.__get__("Google"))
btn1.place(x=50, y=290)

btn2 = customtkinter.CTkButton(master=frame, width=100, image=img3, text="Facebook", height=20, corner_radius=6, compound="left", text_color = "black", fg_color="white", command=available.__get__("Facebook"))
btn2.place(x=170, y=290)


app.mainloop()
