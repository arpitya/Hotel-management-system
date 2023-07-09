from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem


class Login_window:
    def __init__(self, root):
        self.root = root
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\KIIT\Desktop\summer_project\Hotel_mangement_system\images\hotel_images\back.jpg")

        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\KIIT\Desktop\summer_project\Hotel_mangement_system\images\hotel_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        lbl_str = Label(frame, text="Getting Started", font=("Times New Roman",20, "bold"),fg="white",bg="black")
        lbl_str.place(x=80,y=100)
        
        #label
        
        username=lbl=Label(frame,text="Username",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser = ttk.Entry(frame, font=("Times New Roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        
        password=lbl=Label(frame,text="Password",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass = ttk.Entry(frame, font=("Times New Roman", 15, "bold"),show="*")
        self.txtpass.place(x=40, y=250, width=270)
        
        #icon image
        img2=Image.open(r"C:\Users\KIIT\Desktop\summer_project\Hotel_mangement_system\images\hotel_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"C:\Users\KIIT\Desktop\summer_project\Hotel_mangement_system\images\hotel_images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        #login button 
        lgnbtn=Button(frame,text="Login",command=self.login,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        lgnbtn.place(x=110,y=300,width=120,height=35)
        
        #registration button 
        registrationbtn=Button(frame,text="New User Registration",font=("Times New Roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registrationbtn.place(x=15,y=350,width=160)
        
        #forget button 
        forgetbtn=Button(frame,text="Forget Password",font=("Times New Roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=370,width=160)
        
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "12345":
            messagebox.showinfo("Success", "Welcome to Hostel Management System, You are logged in as admin")
            self.Hotel()
        else:
            messagebox.showerror("Invalid", "Invalid username and password")
            
            
    def Hotel(self):
        self.new_window = Toplevel(self.root)
        self.app = HotelManagementSystem(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()


