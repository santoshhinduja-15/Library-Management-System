import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from pymysql import *


class LibraryManagementSystem:

    # ------------------------------------------- database ---------------------------------------------
    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.databorrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def add_data(self):
        try:
            con = connect(host="localhost", user="root", password="Santosh@15", database="mini_project")
            cur = con.cursor()
            cur.execute(
                "insert into library values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.member_var.get(),
                    self.prn_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.author_var.get(),
                    self.databorrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue_var.get(),
                    self.finalprice_var.get()
                ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted successfully")
        except Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def fetch_data(self):
        con = connect(host="localhost", user="root", password="Santosh@15", database="mini_project")
        cur = con.cursor()
        cur.execute("SELECT * FROM library")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            con.commit()
        con.close()

    def show_data(self):
        self.txtBox.delete("1.0", END)
        self.txtBox.insert(END, "Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "FirstName:\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName:\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2: \t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No:\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Auther:\t\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END, "DateBorrowed:\t\t" + self.databorrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue: \t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook: \t\t" + self.daysonbook.get() + "\n")
        self.txtBox.insert(END, "LateRateFine: \t\t" + self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue:\t\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.txtBox.delete("1.0", END)
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.databorrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")

    def delete_data(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "First Select the Member")

        else:
            con = connect(host="localhost", user="root", password="Santosh@15", database="mini_project")
            cur = con.cursor()
            query = "DELETE FROM library WHERE prn_no = %s"
            value = (self.prn_var.get())
            cur.execute(query, value)
            self.txtBox.delete("1.0", END)
            con.commit()
            self.fetch_data()
            self.reset()
            con.close()
            messagebox.showinfo("Success", "Member Deleted Successfully")

    def update_data(self):
        con = connect(host="localhost", user="root", password="Santosh@15", database="mini_project")
        cur = con.cursor()

        sql_query = "UPDATE library SET member=%s, prn_no=%s, id=%s, first_name=%s, last_name=%s, address1=%s, address2=%s, postid=%s, mobile=%s WHERE prn_no=%s"
        data = (
            self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(), self.mobile_var.get(),
            self.prn_var.get()
        )

        cur.execute(sql_query, data)

        con.commit()
        self.fetch_data()
        self.reset()
        con.close()
        messagebox.showinfo("Success", "Member Updated")

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if iExit > 0:
            self.root.destroy()
        else:
            return

    def __init__(self, Root):
        self.root = Root
        self.root.title("Library Management System")
        self.root.geometry("1600x1500")

        # ------------------------------------ variable ------------------------------------------------
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.databorrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()

        lbltitle = Label(self.root, text="Library Management System", bg="powder blue", fg="green", bd=20,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # ==============================Data frame Left=========================================

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=12,
                                   font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 15, "bold"),
                          padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky="w")

        self.textMember = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.member_var)
        self.textMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky="w")
        self.txtPRN_No = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.prn_var)
        self.txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, bg="powder blue", text="ID No", font=("aerial", 12, "bold"), padx=2, pady=4)
        lblTitle.grid(row=2, column=0, sticky="w")
        self.txtTitle = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.id_var)
        self.txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("aerial", 12, "bold"), padx=2,
                             pady=6)
        lblFirstName.grid(row=3, column=0, sticky="w")
        self.txtFirstName = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.firstname_var)
        self.txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("aerial", 12, "bold"), padx=2,
                            pady=6)
        lblLastName.grid(row=4, column=0, sticky="w")
        self.txtLastName = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.lastname_var)
        self.txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address1", font=("aerial", 12, "bold"), padx=2,
                            pady=6)
        lblAddress1.grid(row=5, column=0, sticky="w")
        self.txtAddress1 = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.address1_var)
        self.txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address2", font=("aerial", 12, "bold"), padx=2,
                            pady=6)
        lblAddress2.grid(row=6, column=0, sticky="w")
        self.txtAddress2 = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.address2_var)
        self.txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("aerial", 12, "bold"), padx=2,
                            pady=4)
        lblPostCode.grid(row=7, column=0, sticky="w")
        self.txtPostCode = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.postcode_var)
        self.txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile No", font=("aerial", 12, "bold"), padx=2,
                          pady=6)
        lblMobile.grid(row=8, column=0, sticky="w")
        self.txtMobile = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.mobile_var)
        self.txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book Id", font=("aerial", 12, "bold"), padx=2)
        lblBookId.grid(row=0, column=2, sticky="w")
        self.txtBookId = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.bookid_var)
        self.txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("aerial", 12, "bold"), padx=2,
                             pady=6)
        lblBookTitle.grid(row=1, column=2, sticky="w")
        self.txtBookTitle = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.booktitle_var)
        self.txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author Name", font=("aerial", 12, "bold"), padx=2,
                          pady=6)
        lblAuthor.grid(row=2, column=2, sticky="w")
        self.txtAuthor = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.author_var)
        self.txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("aerial", 12, "bold"),
                                padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky="w")
        self.txtDateBorrowed = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29,
                                     textvariable=self.databorrowed_var)
        self.txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("aerial", 12, "bold"), padx=2,
                           pady=6)
        lblDateDue.grid(row=4, column=2, sticky="w")
        self.txtDateDue = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.datedue_var)
        self.txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days On Book", font=("aerial", 12, "bold"), padx=2,
                              pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky="w")
        self.txtDaysOnBook = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29, textvariable=self.daysonbook)
        self.txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("aerial", 12, "bold"),
                                  padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky="w")
        self.txtLateReturnFine = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29,
                                       textvariable=self.lateratefine_var)
        self.txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("aerial", 12, "bold"),
                               padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky="w")
        self.txtDateOverDue = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29,
                                    textvariable=self.dateoverdue_var)
        self.txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("aerial", 12, "bold"),
                               padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky="w")
        self.txtActualPrice = Entry(DataFrameLeft, font=("aerial", 13, "bold"), width=29,
                                    textvariable=self.finalprice_var)
        self.txtActualPrice.grid(row=8, column=3)

        # =============================DATA FRAME RIGHT==================================================

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12,
                                    font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=870, y=5, width=580, height=350)

        self.txtBox = Text(DataFrameRight, font=("aerial", 12, "bold"), width=40, height=20, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = ['C', 'Python', 'JavaScript', 'Java', 'Effective Java', 'Eloquent JavaScript', 'Learning SQL',
                     'Ruby', 'PHP']

        def SelectBook(event=""):
            if listbox.curselection():
                index = listbox.curselection()[0]
                value = listbox.get(index)
                x = value

                if x == "C":
                    self.bookid_var.set("001")
                    self.booktitle_var.set("C")
                    self.author_var.set("Dennis Ritchie")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 1,700")

                if x == "Python":
                    self.bookid_var.set("002")
                    self.booktitle_var.set("Python")
                    self.author_var.set("Eric Matthes")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 1,850")

                if x == "JavaScript":
                    self.bookid_var.set("003")
                    self.booktitle_var.set("JavaScript")
                    self.author_var.set("Douglas Crockford")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 1,300")

                if x == "Java":
                    self.bookid_var.set("005")
                    self.booktitle_var.set("Java")
                    self.author_var.set("Herbert Schildt")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 1,750")

                if x == "Effective Java":
                    self.bookid_var.set("006")
                    self.booktitle_var.set("Effective Java")
                    self.author_var.set("Joshua Bloch")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 950")

                if x == "Eloquent JavaScript":
                    self.bookid_var.set("007")
                    self.booktitle_var.set("Eloquent Javascript")
                    self.author_var.set("Marjin Haverbeke")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 550")

                if x == "Learning SQL":
                    self.bookid_var.set("008")
                    self.booktitle_var.set("Learning SQL")
                    self.author_var.set("Alan Beaulieu")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 650")

                if x == "Ruby":
                    self.bookid_var.set("009")
                    self.booktitle_var.set("Programming Ruby: The Pragmatic Programmers Guide")
                    self.author_var.set("Eric Freeman")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 750")

                if x == "PHP":
                    self.bookid_var.set("010")
                    self.booktitle_var.set("PHP and MySQL Web Development")
                    self.author_var.set("Laura Thomson")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.databorrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set("15")
                    self.lateratefine_var.set("rs: 50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs. 750")

        listbox = Listbox(DataFrameRight, font=("aerial", 12, "bold"), width=20, height=20)
        listbox.bind("<<ListboxSelect>>", SelectBook)
        listbox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listbox.yview)

        for item in listBooks:
            listbox.insert(END, item)

        # =====================================Buttons Frame========================================

        Framebutton = Frame(self.root, bd=12, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(Framebutton, text="Add Data", font=("aerial", 12, "bold"), width=23, bg="blue", fg="white",
                            command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text="Show Data", font=("aerial", 12, "bold"), width=23, bg="blue", fg="white",
                            command=self.show_data)

        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton, text="Update", font=("aerial", 12, "bold"), width=23, bg="blue", fg="white",
                            command=self.update_data)
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete", font=("aerial", 12, "bold"), width=23, bg="blue", fg="white",
                            command=self.delete_data)
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=("aerial", 12, "bold"), width=23, bg="blue", fg="white",
                            command=self.reset)
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=("aerial", 12, "bold"), width=23, bg="blue", fg="white",
                            command=self.iExit)
        btnAddData.grid(row=0, column=5)

        # ------------------------------ Information Frame ---------------------------------------------------------
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column=(
            "Member Type", "PRN NO", "Title", "First Name", "Last Name", "Address 1", "Address 2", "Post Id", "Mobile",
            "Book Id", "Book Title", "Author", "Date Borrowed", "Date Due", "Days", "Late Return Fine", "Date Over Due",
            "Final Price"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member Type", text="Member Type")
        self.library_table.heading("PRN NO", text="PRN No.")
        self.library_table.heading("Title", text="Title")
        self.library_table.heading("First Name", text="First Name")
        self.library_table.heading("Last Name", text="Last Name")
        self.library_table.heading("Address 1", text="Address1")
        self.library_table.heading("Address 2", text="Address2")
        self.library_table.heading("Post Id", text="Post ID")
        self.library_table.heading("Mobile", text="Mobile Number")
        self.library_table.heading("Book Id", text="Book ID")
        self.library_table.heading("Book Title", text="Book Title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("Date Borrowed", text="Date of Borrowed")
        self.library_table.heading("Date Due", text="Date Due")
        self.library_table.heading("Days", text="Days on Book")
        self.library_table.heading("Late Return Fine", text="Late Return Fine")
        self.library_table.heading("Date Over Due", text="Date Overdue")
        self.library_table.heading("Final Price", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Member Type", width=100)
        self.library_table.column("PRN NO", width=100)
        self.library_table.column("Title", width=100)
        self.library_table.column("First Name", width=100)
        self.library_table.column("Last Name", width=100)
        self.library_table.column("Address 1", width=100)
        self.library_table.column("Address 2", width=100)
        self.library_table.column("Post Id", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("Book Id", width=100)
        self.library_table.column("Book Title", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("Date Borrowed", width=100)
        self.library_table.column("Date Due", width=100)
        self.library_table.column("Days", width=100)
        self.library_table.column("Late Return Fine", width=100)
        self.library_table.column("Date Over Due", width=100)
        self.library_table.column("Final Price", width=100)
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)


root = Tk()
obj = LibraryManagementSystem(root)
root.mainloop()
