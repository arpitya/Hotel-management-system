from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
from time import strftime
from datetime import datetime
import mysql.connector  # pip install mysql-connector-python

class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("1295x550+230+220")

        # varibales
        self.var_conatct = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
# title
        lbl_title = Label(self.root, text="Room Booking", font=(
            "Times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo image
        img2 = Image.open("images\hotel_images\logohotel.png")
        # LANCZOS -> Converts high level image to low level image
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=(
            "Times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # labels andd entry
        # cust_contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_cust_contact = ttk.Entry(
            labelframeleft, textvariable=self.var_conatct, width=20, font=("arial", 13, "bold"))
        entry_cust_contact.grid(row=0, column=1, sticky=W)

        # Featch data button
        btnfetchdata = Button(labelframeleft, command=self.fetch_contact, text="Fetch data", font=(
            "arial", 9, "bold"), bg="black", fg="gold", width=8)
        btnfetchdata.place(x=347, y=4)

        # Check In date
        lbl_checkin = Label(labelframeleft, text="Check in Date:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_checkin.grid(row=1, column=0, sticky=W)

        entry_checkin = ttk.Entry(
            labelframeleft, textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"))
        entry_checkin.grid(row=1, column=1)

        # Check out date
        lbl_checkout = Label(labelframeleft, text="Check out Date:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_checkout.grid(row=2, column=0, sticky=W)

        entry_checkout = ttk.Entry(
            labelframeleft, textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"))
        entry_checkout.grid(row=2, column=1)

        # Room type
        lbl_roomtype = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Room Type: ", padx=2, pady=6)
        lbl_roomtype.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        rowss=my_cursor.fetchall()
        
        combo_roomtype = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_roomtype["value"] = rowss
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3, column=1)

        # Room Avaiblity
        lbl_available_room = Label(labelframeleft, text="Available Room:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_available_room.grid(row=4, column=0, sticky=W)
        
        conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        
        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)
        
        # entry_available_room = ttk.Entry(
        #     labelframeleft, textvariable=self.var_roomavailable, width=29, font=("arial", 13, "bold"))
        # entry_available_room.grid(row=4, column=1)

        # Room Meal
        lbl_Meal = Label(labelframeleft, text="Meal:",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Meal.grid(row=5, column=0, sticky=W)

        # entry_Meal = ttk.Entry(labelframeleft, textvariable=self.var_meal, width=29,
        #                        font=("arial", 13, "bold"))
        # entry_Meal.grid(row=5, column=1)
        entry_Meal = ttk.Combobox(labelframeleft, textvariable=self.var_meal, font=("arial", 12, "bold"), width=27,state="readonly")
        entry_Meal["value"] = ("Nothing","Breakfast", "Lunch","Dinner","All")
        entry_Meal.current(0)
        entry_Meal.grid(row=5, column=1)

        # No. of days
        lbl_noofdays = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="No. of Days: ", padx=2, pady=6)
        lbl_noofdays.grid(row=6, column=0, sticky=W)

        combo_noofdays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays,width=29, font=(
            "arial", 12, "bold"))
        combo_noofdays.grid(row=6, column=1)

        # Paid Tax
        lbl_Paid_Tax = Label(labelframeleft, text="Paid tax:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_Paid_Tax.grid(row=7, column=0, sticky=W)

        entry_Paid_Tax = ttk.Entry(
            labelframeleft, textvariable=self.var_paidtax, width=29, font=("arial", 13, "bold"))
        entry_Paid_Tax.grid(row=7, column=1)

        # Sub total
        lbl_Sub_total = Label(labelframeleft, text="Sub total:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_Sub_total.grid(row=8, column=0, sticky=W)

        entry_Sub_total = ttk.Entry(
            labelframeleft, textvariable=self.var_actualtotal, width=29, font=("arial", 13, "bold"))
        entry_Sub_total.grid(row=8, column=1)

        # Total Cost
        lbl_Total_Cost = Label(labelframeleft, text="Total Cost:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_Total_Cost.grid(row=9, column=0, sticky=W)

        entry_Total_Cost = ttk.Entry(
            labelframeleft, textvariable=self.var_total, width=29, font=("arial", 13, "bold"))
        entry_Total_Cost.grid(row=9, column=1)

        # Bill Button
        btnBill = Button(labelframeleft, text="Bill",command=self.total, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # Buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # right side image
        img3 = Image.open(r"C:\Users\KIIT\Desktop\summer_project\Hotel_mangement_system\images\hotel_images\bed.jpg")
        img3 = img3.resize((520, 300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        # Table frame for search
        Tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and Search System", font=(
            "Times new roman", 12, "bold"), padx=2)
        Tableframe.place(x=435, y=280, width=860, height=260)

        lblsearchby = Label(Tableframe, font=(
            "arial", 12, "bold"), text="Search By: ", bg="red", fg="white")
        lblsearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Tableframe, textvariable=self.search_var, font=(
            "arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Contact", "roomavailable")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(
            Tableframe, width=24, textvariable=self.txt_search, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Tableframe, text="Search",command=self.search, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Tableframe, text="Show All",command=self.fetch_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show Data TAble
        details_table = Frame(Tableframe, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("contact", "checkin", "checkout", "roomtype",
                                       "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Mobile")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="Noofdays")
        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_conatct.get() == "" or self.var_checkin.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values (%s, %s, %s, %s, %s, %s, %s)", (
                                                                                            self.var_conatct.get(),
                                                                                            self.var_checkin.get(),
                                                                                            self.var_checkout.get(),
                                                                                            self.var_roomtype.get(),
                                                                                            self.var_roomavailable.get(),
                                                                                            self.var_meal.get(),
                                                                                            self.var_noofdays.get()
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning!", f"Something went wrong: {str(es)}", parent=self.root) 
    
    
    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cuersor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_conatct.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
        
    def update(self):
        if self.var_conatct.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE room SET checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s WHERE contact=%s", (
                                                                                                                                        self.var_checkin.get(),
                                                                                                                                        self.var_checkout.get(),
                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                        self.var_meal.get(),
                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                        self.var_conatct.get()
                                                                                                                                    ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)
            
    def mDelete(self):
        mDelete = messagebox.askyesno("Hostel Management System", "Do you want to delete this Customer details", parent=self.root)
        if mDelete:
            conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
            my_cursor = conn.cursor()
            query = "DELETE FROM room WHERE contact=%s"
            value = (self.var_conatct.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Delete", "Customer details have been deleted successfully", parent=self.root)

    def reset(self):
        self.var_conatct.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        
# All Data fetch
    def fetch_contact(self):
        if self.var_conatct.get() == "":
            messagebox.showerror(
                "Error", "Please enter Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", port="3307", username="root", password="123456789", database="management")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_conatct.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "This number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=450, y=55, width=300, height=200)

                lblName = Label(showDataFrame, text="Name:",
                                font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row,
                            font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # gender
                conn = mysql.connector.connect(
                    host="localhost", port="3307", username="root", password="123456789", database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_conatct.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataFrame, text="Gender:",font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataFrame, text=row,font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                # Email
                conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_conatct.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataFrame, text="Email:",font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataFrame, text=row,font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                # Nationality
                conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_conatct.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataFrame, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl4 = Label(showDataFrame, text=row,font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                # Address
                conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_conatct.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataFrame, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5 = Label(showDataFrame, text=row,font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)
                
                # Meal
                conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
                my_cursor = conn.cursor()
                query = ("select meal from room where contact=%s")
                value = (self.var_conatct.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblMeals = Label(showDataFrame, text="Meal:", font=("arial", 12, "bold"))
                lblMeals.place(x=0, y=150)

                lbl5 = Label(showDataFrame, text=row,font=("arial", 12, "bold"))
                lbl5.place(x=90, y=150)
    
    #search system
    def search(self):
        conn = mysql.connector.connect(host="localhost", port="3307", username="root", password="123456789", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")


        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def total(self):
        inDate=self.var_checkin.get()            
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(100)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(280)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(350)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(280)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(350)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(280)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(350)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Nothing" and self.var_roomtype.get()=="Single"):
            q1=float(0)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Nothing" and self.var_roomtype.get()=="Double"):
            q1=float(0)
            q2=float(650)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Nothing" and self.var_roomtype.get()=="Luxury"):
            q1=float(0)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Single"):
            q1=float(730)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Double"):
            q1=float(730)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Luxury"):
            q1=float(730)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.09))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
