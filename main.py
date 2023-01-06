import sqlite3
from tkinter import *
import customtkinter
from tkinter import ttk
from PIL import Image, ImageTk

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

#Create a Ctk instance(app)
main = customtkinter.CTk()
main.geometry("400x240")
main.resizable(width=False, height=False)

#Username Frame
username_tittle = customtkinter.CTkLabel(master=main, text='Username:').place(relx=0.2, rely= 0.3)
username_box = customtkinter.CTkEntry(master=main, width=150)
username_box.place(relx=0.43, rely=0.3)
python_image = ImageTk.PhotoImage(Image.open('logo.png'), Image.ANTIALIAS, )
but = customtkinter.CTkLabel(master=main, image=python_image, text='', width=50, height=50).place(relx=0.4, rely = 0.05)

#Password Frame
password_tittle = customtkinter.CTkLabel(master=main, text='Password:').place(relx=0.2, rely= 0.45)
password_box = customtkinter.CTkEntry(master=main,width=150, show='*')
password_box.place(relx=0.43, rely=0.45)

#Enter and SigUp Buttons
enter_buttom = customtkinter.CTkButton(master=main, text='Enter', width=100)
enter_buttom.place(relx=0.33, rely=0.8, anchor=CENTER)

signup_buttom = customtkinter.CTkButton(master=main, text='SignUp', width=100)
signup_buttom.place(relx=0.67, rely=0.8, anchor=CENTER)


main.mainloop()