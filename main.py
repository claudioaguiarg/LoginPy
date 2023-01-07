import sqlite3
from tkinter import *
import customtkinter
from tkinter import ttk
from PIL import Image, ImageTk

con = sqlite3.connect("base.db")
cur = con.cursor()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

class SistemaLogin():
    def __init__(self) -> None:
       #Create a Ctk instance(app)
        self.main = customtkinter.CTk()
        self.main.geometry("400x240")
        self.main.resizable(width=False, height=False)

        #Username Frame
        username_tittle = customtkinter.CTkLabel(master=self.main, text='Username:').place(relx=0.2, rely= 0.3)
        self.username_box = customtkinter.CTkEntry(master=self.main, width=150)
        self.username_box.place(relx=0.43, rely=0.3)
        python_image = ImageTk.PhotoImage(Image.open('logo.png') )
        but = customtkinter.CTkLabel(master=self.main, image=python_image, text='', width=50, height=50).place(relx=0.4, rely = 0.05)

        #Password Frame
        password_tittle = customtkinter.CTkLabel(self.main, text='Password:').place(relx=0.2, rely= 0.45)
        self.password_box = customtkinter.CTkEntry(self.main,width=150, show='*')
        self.password_box.place(relx=0.43, rely=0.45)

        #Enter and SigUp Buttons
        enter_buttom = customtkinter.CTkButton(self.main, text='Enter', width=100, command=self.loginAuthorization)
        enter_buttom.place(relx=0.33, rely=0.8, anchor=CENTER)

        signup_buttom = customtkinter.CTkButton(self.main, text='Register', width=100, command=self.register)
        signup_buttom.place(relx=0.67, rely=0.8, anchor=CENTER)


        self.main.mainloop()

    def register(self):
        self.main.destroy()
        self.main = customtkinter.CTk()
        self.main.geometry("400x240")
        self.main.resizable(width=False, height=False)

        #Username box register
        username_tittle = customtkinter.CTkLabel(master=self.main, text='Username:').place(relx=0.2, rely= 0.3)
        self.username_box_register = customtkinter.CTkEntry(master=self.main,width=150)
        self.username_box_register.place(relx=0.43, rely=0.3)
        
        #Password box reister
        password_tittle = customtkinter.CTkLabel(self.main, text='Password:').place(relx=0.2, rely= 0.45)
        self.password_register_box = customtkinter.CTkEntry(self.main,width=150, show='*')
        self.password_register_box.place(relx=0.43, rely=0.45)

        #Register buttom
        self.signup_buttom = customtkinter.CTkButton(self.main, text='Register', width=100, command=self.register_db)
        self.signup_buttom.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.main.mainloop()

    def register_db(self):
        username = self.username_box_register.get()
        password = self.password_register_box.get()
        try:
            cur.execute(f"""
                        INSERT INTO users VALUES
                        ('{username}','{password}')
                        """)
            con.commit()
            print('Sucess')
        except:
            print('Fail')
        
        

    #Define a function that verify the authorization
    def loginAuthorization(self):
        #verifica username na db
        try:
            username = self.username_box.get()
            res = cur.execute(f"SELECT * FROM users WHERE name='{username}'")
            res = res.fetchall()
        except:
            print('Database connection error')

        #verifica password na db
        try:
            password = self.password_box.get()
        except:
            print('Password get-error')

        #se autorizado, deleta a main e inicia a pagina de autorização
        try:
            if password == res[0][1]:
                print('Sucess')
            else:
                print('Wrong username or password')
        except:
            print('Database error')
        #senão mostra mensagem de erro
    

#Create a Ctk instance(app)
main = SistemaLogin()
main()