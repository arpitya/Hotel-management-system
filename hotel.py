from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from customer import Cust_win
from room import RoomBooking
from details import DetailsRoom
from report import report


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("1550x800+0+0")
        # 1st image
        img1 = Image.open("images\hotel_images\hotel1.png")
        # LANCZOS -> Converts high level image to low level image
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # Logo image
        img2 = Image.open("images\hotel_images\logohotel.png")
        # LANCZOS -> Converts high level image to low level image
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        # title
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
            "Times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # IN FRAME
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)
        # menu0
        lbl_menu = Label(main_frame, text="MENU", font=(
            "Times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        # menu
        btn_frame = Label(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="Customer", command=self.cust_details, width=20, font=(
            "Times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="Room", command=self.roombooking, width=20, font=(
            "Times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        detail_btn = Button(btn_frame, text="Details",command=self.DetailsRoom, width=20, font=(
            "Times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        detail_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="Report",command=self.report, width=20, font=(
            "Times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame,command=self.logout, text="Log out", width=20, font=(
            "Times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # right side image
        img3 = Image.open("images\hotel_images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1310, height=590)

        # down image
        img4 = Image.open("images\hotel_images\myh.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

        # img5=Image.open("images\hotel_images\khana.jpg")
        # img5=img5.resize((230,190),Image.LANCZOS)
        # self.photoimg5=ImageTk.PhotoImage(img5)

        # lblimg1=Label(main_frame,image=self.photoimg5,bd=5,relief=RIDGE)
        # lblimg1.place(x=0,y=420,width=230,height=190)
        lbl_name = Label(main_frame, text="Created by Arpitya", font=(
            "Times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_name.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)
        
    def DetailsRoom(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)
    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = report(self.new_window)
        
    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
