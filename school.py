import mysql.connector
import os
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


def registration_window():
    os.system('python registration.py')


def abt():
    showinfo("Notepad", "Notepad by code with Namrata "
                        "this program is created on based on collage registration "
                        "and to show login and registration working with mysql database")


def entry_clear(e):
    if txtuser.get() == 'Username' or txtpass.get() == 'Password':
        txtuser.delete(0, END)
        txtpass.delete(0, END)
        txtpass.config(show="*")


def login():
    def reset_phone():
        if security_c.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=root3)
        elif txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=root3)
        elif txt_newno.get() == "":
            messagebox.showerror("Error", "Please enter the new Mobile Number", parent=root3)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="290393", database="test")
            my_cursor = conn.cursor()
            query1 = "select * from register where emailid=%s and security=%s and answer=%s"
            value1 = (txtuser.get(), security_c.get(), txt_security.get(),)
            my_cursor.execute(query1, value1)
            row1 = my_cursor.fetchone()
            if row1 == None:
                messagebox.showerror("Error", " Please enter the correct answer", parent=root3)
            else:
                query2 = "update register set mobileno=%s where emailid=%s"
                value2 = (txt_newno.get(), txtuser.get())
                my_cursor.execute(query2, value2)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", " Your Mobile Number hss been updated ", parent=root3)
                root3.destroy()
    if txtuser.get() == "" or txtpass.get() == "":
        messagebox.showerror("Error", "all field required")
    else:
        conn = mysql.connector.connect(host="localhost", user="root", password="290393", database="test")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from register where emailid=%s and password=%s", (txtuser.get(),
                                                                                      txtpass.get()
                                                                                      ))
        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Invalid Username and Password")
        else:
            conn.commit()
            conn.close()
            detail = ""
            for i in row:
                detail = {"Name: ": row[0]+" "+row[1]+" "+row[2],
                          "Gender ": row[3],
                          "Father Name ": row[4],
                          "Mobile no: ": row[5],
                          "Email id ": row[6],
                          "10th Marks ": row[7],
                          "10th School ": row[8],
                          "12th School ": row[9],
                          "12th Marks ": row[10],
                          "Collage ": row[11],
                          "Password ": row[12],
                          "Security Question ": row[13],
                          "Security Answer ": row[14]}
            # print(*[str(key) + ":" + str(value) for key, value in detail.items()], sep='\n')
            '''for x, y in detail.items():
                print(x, ":", y)
                str(detail).replace(', ', '\n ')'''
            line_format = '%s : %s'
            ans = messagebox.askyesno("Do you Want to edit ", message="\n".join([line_format % (key, str(value))
                                                                                 for key, value in detail.items()
                                                                                 ]))
            if ans == YES:
                root3 = Toplevel()
                root3.title("forget password")
                root3.geometry("340x450+610+170")
                lab = Label(root3, text="Edit Phone Number", font=("times new roman", 15, "bold"), fg="red", bg="white")
                lab.place(x=0, y=10, relwidth=1)
                security = Label(root3, text="Security Question:", font=('times new roman', 15, "bold"), bg="white")
                security.place(x=50, y=80)
                security_c = ttk.Combobox(root3, font=("Times New Roman", 12, "bold"), state="readonly",
                                          justify='center', width=29)
                security_c["values"] = ("Select", "Your birth place ?", "Your mother name ?", "Your favourite place ?",
                                        "Your pet name ?")
                security_c.place(x=50, y=110, anchor="nw")
                security_c.current(0)
                security_a = Label(root3, text="Security Answer :", font=("veradana", 12), bg="white")
                security_a.place(x=50, y=150)
                txt_security = ttk.Entry(root3, width=30, font=('times new roman', 15, "bold"))
                txt_security.place(x=50, y=180, anchor="nw", width=250)

                new_mobile = Label(root3, text=" New Mobile No:", font=("veradana", 12), bg="white")
                new_mobile.place(x=50, y=220)
                txt_newno = ttk.Entry(root3, width=30, font=('times new roman', 15, "bold"))
                txt_newno.place(x=50, y=250, anchor="nw", width=250)

                btn = Button(root3, text="Reset", font=('times new roman', 15, "bold"), fg="white", bg="Black",
                             command=reset_phone)
                btn.place(x=120, y=290)


def forget_password():
    def reset_password():
        if security_c.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=root2)
        elif txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=root2)
        elif txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="290393", database="test")
            my_cursor = conn.cursor()
            query1 = "select * from register where emailid=%s and security=%s and answer=%s"
            value1 = (txtuser.get(), security_c.get(), txt_security.get(),)
            my_cursor.execute(query1, value1)
            row1 = my_cursor.fetchone()
            if row1 == None:
                messagebox.showerror("Error", " Please enter the correct answer", parent=root2)
            else:
                query2 = "update register set password=%s where emailid=%s"
                value2 = (txt_newpass.get(), txtuser.get())
                my_cursor.execute(query2, value2)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", " your Password has been reset, Please Login new password", parent=root2)
                root2.destroy()

    if txtuser.get() == "":
        messagebox.showerror("Error", "Please enter the email address to reset password")
    else:
        conn = mysql.connector.connect(host="localhost", user="root", password="290393", database="test")
        my_cursor = conn.cursor()
        query = "select * from register where emailid=%s"
        value = (txtuser.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()
        print(row)

        if row == None:
            messagebox.showerror("My Error", "Please enter the valid username")
        else:
            conn.close()
            root2 = Toplevel()
            root2.title("forget password")
            root2.geometry("340x450+610+170")
            root2.resizable(False, False)

            lab = Label(root2, text=" Forgot Password", font=("times new roman", 15, "bold"), fg="red", bg="white")
            lab.place(x=0, y=10, relwidth=1)
            security = Label(root2, text="Security Question:", font=('times new roman', 15, "bold"), bg="white")
            security.place(x=50, y=80)
            security_c = ttk.Combobox(root2, font=("Times New Roman", 12, "bold"), state="readonly", justify='center',
                                      width=29)
            security_c["values"] = ("Select", "Your birth place", "Your mother name", "Your favourite place",
                                    "Your pet name")
            security_c.place(x=50, y=110, anchor="nw")
            security_c.current(0)
            security_a = Label(root2, text="Security Answer :", font=("veradana", 12), bg="white")
            security_a.place(x=50, y=150)
            txt_security = ttk.Entry(root2, width=30, font=('times new roman', 15, "bold"))
            txt_security.place(x=50, y=180, anchor="nw", width=250)

            new_password = Label(root2, text=" New Password:", font=("veradana", 12), bg="white")
            new_password.place(x=50, y=220)
            txt_newpass = ttk.Entry(root2, width=30, font=('times new roman', 15, "bold"))
            txt_newpass.place(x=50, y=250, anchor="nw", width=250)

            btn = Button(root2, text="Reset", font=('times new roman', 15, "bold"), fg="white", bg="Black",
                         command=reset_password)
            btn.place(x=120, y=290)


def professor():
    r = Tk()
    r.title('Details')
    r.geometry("1350x550")
    r.resizable(False, False)
    conn = mysql.connector.connect(host="localhost", user="root", password="290393", database="test")
    my_cursor = conn.cursor()
    my_cursor.execute("Select * from register")
    row = my_cursor.fetchall()

    s = ttk.Style(r)
    s.theme_use("clam")
    s.configure('Treeview.Heading', background="light green", relief='flat')
    s.map('Treeview.Heading', background=[('active', 'light green')])

    tree_scroll = Scrollbar(r)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll1 = Scrollbar(r, orient=HORIZONTAL)
    tree_scroll1.pack(side=BOTTOM, fill=X)
    my_tree = ttk.Treeview(r, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll1.set,
                           selectmode="extended", height=25)
    my_tree['columns'] = ("First", "Middle", "Last", "Gender", "Father", "MobileNo", "EmailId", "10thMarks",
                          "10thSchool", "12thSchool", "12thMarks", "Collage", "Password", "SecurityQ", "SecurityA")
    tree_scroll.config(command=my_tree.yview)
    tree_scroll1.config(command=my_tree.xview)
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("First", anchor=W, width=90)
    my_tree.column("Middle", anchor=W, width=90, stretch=NO)
    my_tree.column("Last", anchor=W, width=90)
    my_tree.column("Gender", anchor=W, width=60)
    my_tree.column("Father", anchor=W, width=120)
    my_tree.column("MobileNo", anchor=CENTER, width=70)
    my_tree.column("EmailId", anchor=W, width=180)
    my_tree.column("10thMarks", anchor=CENTER, width=70)
    my_tree.column("10thSchool", anchor=W, width=130)
    my_tree.column("12thSchool", anchor=W, width=130)
    my_tree.column("12thMarks", anchor=CENTER, width=70)
    my_tree.column("Collage", anchor=W, width=100)
    my_tree.column("Password", anchor=CENTER, width=120)
    my_tree.column("SecurityQ", anchor=W, width=130)
    my_tree.column("SecurityA", anchor=W, width=100)

    my_tree.heading("#0", text="S.No.", anchor=W)
    my_tree.heading("First", text="First Name", anchor=W)
    my_tree.heading("Middle", text="Middle Name", anchor=W)
    my_tree.heading("Last", text="Last Name", anchor=W)
    my_tree.heading("Gender", text="Gender", anchor=W)
    my_tree.heading("Father", text="Father Name", anchor=W)
    my_tree.heading("MobileNo", text="Mobile No", anchor=CENTER)
    my_tree.heading("EmailId", text="Email Id", anchor=W)
    my_tree.heading("10thMarks", text="10th Marks", anchor=CENTER)
    my_tree.heading("10thSchool", text="10th School", anchor=W)
    my_tree.heading("12thSchool", text="12th School", anchor=W)
    my_tree.heading("12thMarks", text="12th Marks", anchor=CENTER)
    my_tree.heading("Collage", text="Collage", anchor=W)
    my_tree.heading("Password", text="Password", anchor=CENTER)
    my_tree.heading("SecurityQ", text="Security Question", anchor=W)
    my_tree.heading("SecurityA", text="Security Answer", anchor=W)

    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="grey")
    count = 0
    for i in row:
        # print(i)
        if count % 2 == 0:
            my_tree.insert('', count, text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                                                         i[10], i[11], i[12], i[13], i[14]), tags=('evenrow',))
        else:
            my_tree.insert('', count, text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                                                         i[10], i[11], i[12], i[13], i[14]), tags=('oddrow',))
        count += 1
    '''ro = 0
    for i in row:
        my_tree.insert('', ro, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10],
                                                i[11], i[12], i[13], i[14]))
        ro = ro + 1'''
    my_tree.pack()

    conn.commit()
    conn.close()


if __name__ == '__main__':
    root = Tk()
    root. geometry("1200x437")
    root.resizable(False, False)

    # main page
    img = PhotoImage(file="./school.jpg")
    mylabel = Label(root, image=img)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)
    canvas = Canvas(root, width=1200, height=437)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.create_text(450, 250, text="Welcome to school portal", font=("veradana", 30), fill="white")
    reg = Button(root, text="Registration", command=registration_window)
    pro = Button(root, text="professor", command=professor)
    about = Button(root, text="About", command=abt)
    close = Button(root, text="Close", command=root.destroy)
    # signup = Button(root, text="SignUp")
    # login_window = canvas.create_window(992, 10, anchor="nw", window=signup)
    reg_window = canvas.create_window(1050, 10, anchor="nw", window=reg)
    pro_window = canvas.create_window(1130, 10, anchor="nw", window=pro)
    about_window = canvas.create_window(5, 10, anchor="nw", window=about)
    close_window = canvas.create_window(55, 10, anchor="nw", window=close)
    # login sets
    frame = Frame(root, bg="black")
    frame.place(x=950, y=80, width=190, height=150)
    canvas.create_text(900, 98, text="UserName :", font=("veradana", 12), fill="white")
    canvas.create_text(900, 138, text="Password :", font=("veradana", 12), fill="white")
    # bind the entryboxes
    txtuser = Entry(root, width=30, highlightthickness=2)
    txtpass = Entry(root, width=30, highlightthickness=2)
    txtuser.insert(0, "Username")
    txtpass.insert(0, "Password")
    urn_window = canvas.create_window(950, 90, anchor="nw", window=txtuser)
    pswd_window = canvas.create_window(950, 130, anchor="nw", window=txtpass)
    txtuser.bind("<Button-1>", entry_clear)
    txtpass.bind("<Button-1>", entry_clear)
    # down buttons
    forgot = Button(root, text="forgot password", command=forget_password, borderwidth=0, fg="white", bg="black",)
    forgot_window = canvas.create_window(960, 160, anchor="nw", window=forgot)
    login1 = Button(root, text="Login", relief=RIDGE, fg="black", activebackground="black", command=login)
    signup = Button(root, text="SignUp", fg="black", activebackground="black", command=registration_window)
    login1_window = canvas.create_window(990, 185, anchor="nw", window=login1)
    signup_window = canvas.create_window(1050, 185, anchor="nw", window=signup)
    # main program ends
    root.mainloop()
