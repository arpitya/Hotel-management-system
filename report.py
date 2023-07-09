from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox

class report:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("1295x550+230+220")        
        lbl_title = Label(self.root, text="Hotel Management System", font=(
            "Times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)        
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Report", font=(
            "Times new roman", 15, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=2155, height=490)        
        #Introduction
        lbl_Introduction = Label(labelframeleft, text="Introduction: ", font=("arial", 14, "bold"), padx=2, pady=6)
        lbl_Introduction.grid(row=0, column=0, sticky=W)        
        lbl_Introduction = Label(labelframeleft, text="The Room Booking Details Management System is a GUI application developed using Tkinter and MySQL. It provides functionality for managing room", font=("arial", 12))
        lbl_Introduction.grid(row=0, column=1, sticky=W)
        lbl_Introduction = Label(labelframeleft, text="booking details in a hostel or hotel.", font=("arial", 12))
        lbl_Introduction.grid(row=1, column=1, sticky=W)        
        #Features
        lbl_Features = Label(labelframeleft, text="Features: ", font=("arial", 14, "bold"), padx=2, pady=6)
        lbl_Features.grid(row=2, column=0, sticky=W)        
        lbl_Features = Label(labelframeleft, text="a). Add/Update/Delete/Reset Details:", font=("arial", 12,"bold"), padx=2, pady=6)
        lbl_Features.grid(row=2, column=1, sticky=W)
        lbl_Features = Label(labelframeleft, text="Allows users to add,delete,update,reset new details. Validates the input fields and displays an error message if any field is missing.", font=("arial", 12))
        lbl_Features.grid(row=3, column=1, sticky=W)
        lbl_Features = Label(labelframeleft, text="Updates the Details in Database. Displays a confirmation message to ensure the user's intention.", font=("arial", 12))
        lbl_Features.grid(row=4, column=1, sticky=W)
        lbl_Features = Label(labelframeleft, text="b). View and Search:", font=("arial", 12,"bold"), padx=2, pady=6)
        lbl_Features.grid(row=5, column=1, sticky=W)
        lbl_Features = Label(labelframeleft, text="Displays details in table. Can be scrolled horizontally and vertically to view all the data. Filter and find specific details.", font=("arial", 12))
        lbl_Features.grid(row=6, column=1, sticky=W)
        lbl_Features = Label(labelframeleft, text="Updates the Details in Database. Displays a confirmation message to ensure the user's intention.", font=("arial", 12))
        lbl_Features.grid(row=7, column=1, sticky=W)        
        #Database
        lbl_Database = Label(labelframeleft, text="Database: ", font=("arial", 14, "bold"), padx=2, pady=6)
        lbl_Database.grid(row=8, column=0, sticky=W)        
        lbl_Database = Label(labelframeleft, text="Uses MySQL as DBMS. Establishes a connection to the local MySQL server",font=("arial", 12), padx=2, pady=6)
        lbl_Database.grid(row=8, column=1, sticky=W)       
        #Dependencies
        lbl_Dependencies = Label(labelframeleft, text="Dependencies: ", font=("arial", 14, "bold"), padx=2, pady=6)
        lbl_Dependencies.grid(row=9, column=0, sticky=W)        
        lbl_Dependencies = Label(labelframeleft, text="The code relies on external libraries such as Tkinter, PIL, and mysql-connector-python.",font=("arial", 12), padx=2, pady=6)
        lbl_Dependencies.grid(row=9, column=1, sticky=W)        
        #Conclusion
        lbl_Conclusion = Label(labelframeleft, text="Conclusion: ", font=("arial", 14, "bold"), padx=2, pady=6)
        lbl_Conclusion.grid(row=10, column=0, sticky=W)        
        lbl_Conclusion = Label(labelframeleft, text="The Hostel Booking Management System provides a user-friendly interface for manage bookings in hotel.",font=("arial", 12), padx=2, pady=6)
        lbl_Conclusion.grid(row=10, column=1, sticky=W)
        lbl_Conclusion = Label(labelframeleft, text="It simplifies the process of adding, updating, and deleting room details while offering a convenient search system for quick access to specific room information.",font=("arial", 12), padx=2, pady=6)
        lbl_Conclusion.grid(row=11, column=1, sticky=W)       
        #Created by
        lbl_Created = Label(labelframeleft, text="Created By: ", font=("arial", 14, "bold"), padx=2, pady=6)
        lbl_Created.grid(row=12, column=0, sticky=W)        
        lbl_Created = Label(labelframeleft, text="Arpitya Kumar Singh",font=("arial", 12), padx=2, pady=6)
        lbl_Created.grid(row=12, column=1, sticky=W)      
        #Email
        lbl_Email = Label(labelframeleft, text="Email: ", font=("arial", 14, "bold"), padx=2, pady=6)
        lbl_Email.grid(row=13, column=0, sticky=W)        
        lbl_Email = Label(labelframeleft, text="arpityasingh@gmail.com",font=("arial", 12), padx=2, pady=6)
        lbl_Email.grid(row=13, column=1, sticky=W)
if __name__ == "__main__":
    root = Tk() 
    obj = Cust_win(root)
    root.mainloop()