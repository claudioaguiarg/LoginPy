import sqlite3
from tkinter import *
import customtkinter
from PIL import Image

con = sqlite3.connect("base.db")
cur = con.cursor()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

class SistemaLogin():
    def __init__(self) -> None:
        self.list_destroy = []
        #Create a Ctk instance(app)
        self.main = customtkinter.CTk()
        self.main.geometry("400x240")
        self.main.resizable(width=False, height=False)

        self.feedback = customtkinter.CTkLabel(master=self.main, text='')
        self.feedback.pack(side=BOTTOM)

        self.default()

        self.main.mainloop()

    def default(self):
        #Destroys widgets of others pages(register)
        self.destroy_items()
        #Username Frame
        self.username_tittle = customtkinter.CTkLabel(master=self.main, text='Username:')
        self.username_tittle.place(relx=0.2, rely= 0.3)
        self.username_box = customtkinter.CTkEntry(master=self.main, width=150)
        self.username_box.place(relx=0.43, rely=0.3)
        python_image = customtkinter.CTkImage(Image.open('logo.png'),size=(80,50))
        self.but = customtkinter.CTkLabel(master=self.main, image=python_image, text='', width=50, height=50)
        self.but.place(relx=0.4, rely = 0.05)

        #Password Frame
        self.password_tittle = customtkinter.CTkLabel(self.main, text='Password:')
        self.password_tittle.place(relx=0.2, rely= 0.45)
        self.password_box = customtkinter.CTkEntry(self.main,width=150, show='*')
        self.password_box.place(relx=0.43, rely=0.45)

        #Enter and SigUp Buttons
        self.enter_buttom = customtkinter.CTkButton(self.main, text='Enter', width=100, command=self.loginAuthorization)
        self.enter_buttom.place(relx=0.33, rely=0.8, anchor=CENTER)

        self.signup_buttom = customtkinter.CTkButton(self.main, text='Register', width=100, command=self.register)
        self.signup_buttom.place(relx=0.67, rely=0.8, anchor=CENTER)
        self.list_destroy = [self.username_tittle,
                             self.username_box,
                             self.but,
                             self.password_tittle,
                             self.password_box,
                             self.enter_buttom,
                             self.signup_buttom]
    def register(self):
        #Destroys the main widgets
        self.destroy_items()
        #Username box register
        self.username_tittle = customtkinter.CTkLabel(master=self.main, text='Username:')
        self.username_tittle.place(relx=0.2, rely= 0.3)
        self.username_box_register = customtkinter.CTkEntry(master=self.main,width=150)
        self.username_box_register.place(relx=0.43, rely=0.3)
        
        #Password box reister
        self.password_tittle = customtkinter.CTkLabel(self.main, text='Password:')
        self.password_tittle.place(relx=0.2, rely= 0.45)
        self.password_register_box = customtkinter.CTkEntry(self.main,width=150, show='*')
        self.password_register_box.place(relx=0.43, rely=0.45)

        #Register buttom
        self.return_buttom = customtkinter.CTkButton(self.main, text='Return', width=100, command=self.default)
        self.return_buttom.place(relx=0.33, rely=0.8, anchor=CENTER)

        self.signup_buttom = customtkinter.CTkButton(self.main, text='Register', width=100, command=self.register_db)
        self.signup_buttom.place(relx=0.67, rely=0.8, anchor=CENTER)

        self.list_destroy = [self.username_tittle,
                             self.username_box_register,
                             self.password_tittle,
                             self.password_register_box,
                             self.return_buttom,
                             self.signup_buttom]
        
    #Define a function that registers username and password at DB
    def register_db(self):
        #catch the username and password
        username = self.username_box_register.get()
        password = self.password_register_box.get()
        #virify if username or password is empty
        if len(username) == 0 or len(password) == 0:
            self.feedback_message('The boxes cannot be empty')
        else:
            try:
                #search in database if username already exists
                res = cur.execute(f"SELECT * FROM users WHERE name='{username}'")
                res = res.fetchall()
                if len(res) != 0:
                    self.feedback_message('This username already exist')
                else:
                    try:
                        cur.execute(f"""
                                    INSERT INTO users VALUES
                                    ('{username}','{password}')
                                    """)
                        con.commit()
                        print('Sucess')
                    except:
                        self.feedback_message('ERROR [DATABASE REGISTER]')
            except:
                self.feedback_message('ERROR [USER VALIDATION]')
        
    #Define a function that verify the authorization
    def loginAuthorization(self):
        #verifica username na db
        try:
            username = self.username_box.get()
        except:
            self.feedback_message('Username get-error')

        #verifica password na db
        try:
            password = self.password_box.get()
        except:
            self.feedback_message('Password get-error')

        if len(username) == 0 or len(password) == 0:
            self.feedback_message('The boxes cannot be empty')
        else:
            res = cur.execute(f"SELECT * FROM users WHERE name='{username}'")
            res = res.fetchall()
            if len(res) == 0:
                self.feedback_message('unregistered user')
            else:
                try:
                    if password == res[0][1]:
                        self.feedback_message('Sucess')
                    else:
                        self.feedback_message('Wrong username or password')
                except:
                    self.feedback_message('Database error')
               
    
   
    def destroy_items(self):
        try:
            for item in self.list_destroy:
                item.destroy()
        except:
            self.feedback_message('Error [Destroy Items]')

    def feedback_message(self,message):
        self.feedback.configure(text=message)
        self.feedback.after(5000, self.clear_feedback)

    def clear_feedback(self):
        self.feedback.configure(text='')

#Create a Ctk instance(app)
main = SistemaLogin()
main()