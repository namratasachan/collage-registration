from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import re

root = Tk()
root.title("register")
root.geometry("1350x500")
root.resizable(False, False)
img = PhotoImage(file="./college.jpg")
mylabel = Label(root, image=img)
mylabel.place(x=0, y=0, relwidth=1, relheight=1)
root.attributes('-alpha', 0.90)
canvas = Canvas(root, width=1200, height=437)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=img, anchor="nw")
# frame = Frame(root, bg="white")
# frame.place(x=420, y=90, width=800, height=450)
# variable for database
var_fname = StringVar()
var_mname = StringVar()
var_lname = StringVar()
var_gender = StringVar()
var_fathername = StringVar()
var_mobileno = StringVar()
var_emailid = StringVar()
var_ten = StringVar()
var_tenschool = StringVar()
var_tweleth = StringVar()
var_twelethschool = StringVar()
var_password = StringVar()
var_confpawd = StringVar()
var_collage = StringVar()
var_security = StringVar()
var_check = IntVar()
var_answer = StringVar()


def checkemail(emil):
    if len(emil) > 7:
        if re.match("^([A-Za-z0-9._-]+)@([A-Za-z0-9.-]+).([A-Z|a-z]{2,5})$", emil):
            return True
        else:
            messagebox.showwarning("Alert", " Invalid email. Enter valid email id(ex. kiran@gmail.com")
            return False
    else:
        messagebox.showerror("Invalid", "lenght is to small")


def checkpassword(pasw):
    if len(pasw) <= 21:
        if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-zA-z0-9]))", pasw):
            return True
        else:
            messagebox.showinfo("Invalid", "Enter valid Password(ex. kirsn@123")
            return True
    else:
        messagebox.showerror("Invalid", "length exceeded")
        return True


def checkcontact(contact):
    if contact.isdigit():
        return True
    if len(str(contact)) == 0:
        return True
    else:
        messagebox.showerror("Invalid", "invalid Number")
        return False


# function for submit button
def submit1():
    if var_fname.get() == "" or var_emailid.get() == "" or var_mobileno.get() == "" or var_lname.get() == "" \
            or var_fathername == "":
        messagebox.showerror("Error", "All Fields Are Required")
    elif len(var_mobileno.get()) != 10:
        messagebox.showerror("Error", "mobile no is not correct")
    elif var_ten.get() == "" or var_tenschool.get() == "" or var_tweleth.get() == "" or var_twelethschool == "":
        messagebox.showerror("Error", "enter School details")
    elif var_password.get() != var_confpawd.get():
        messagebox.showerror("Error", "Password and Conform Password Should be same")
    elif var_emailid.get() != NONE and var_password.get() != NONE:
        x = checkemail(var_emailid.get())
        y = checkpassword(var_password.get())
        if(x == TRUE) and (y == TRUE):
            if var_check.get() == 0:
                messagebox.showerror("Error", "Please Agree or terms and condition")
            else:
                messagebox.showinfo("Info", "data is summited")
                conn = mysql.connector.connect(host="localhost", user="root", password="290393", database="test")
                my_cursor = conn.cursor()
                query = "select * from register where emailid=%s"
                value = (var_emailid.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exist, Please try another email")
                else:
                    my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                                var_fname.get(),
                                                                                                var_mname.get(),
                                                                                                var_lname.get(),
                                                                                                var_gender.get(),
                                                                                                var_fathername.get(),
                                                                                                var_mobileno.get(),
                                                                                                var_emailid.get(),
                                                                                                var_ten.get(),
                                                                                                var_tenschool.get(),
                                                                                                var_twelethschool.get(),
                                                                                                var_tweleth.get(),
                                                                                                var_collage.get(),
                                                                                                var_password.get(),
                                                                                                var_security.get(),
                                                                                                var_answer.get()
                                                                                                ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Register Success full")
                    ans = messagebox.askyesno('YES|NO', 'Do you want to register another')
                    if ans == NO:
                       root.destroy()


# text for from start
canvas.create_text(700, 30, text="Register Here", font=("veradana", 20), fill="Black")
fstname = canvas.create_text(150, 80, text="First Name :", font=("veradana", 12), fill="Black")
mdlname = canvas.create_text(590, 80, text="Middle Name :", font=("veradana", 12), fill="Black")
surname = canvas.create_text(1040, 80, text="Surname :", font=("veradana", 12), fill="Black")
gender = canvas.create_text(160, 135, text="Gender :", font=("veradana", 12), fill="Black")
female = canvas.create_text(260, 135, text=": Female", font=("veradana", 12), fill="Black")
male = canvas.create_text(365, 135, text=": Male", font=("veradana", 12), fill="Black")
father_name = canvas.create_text(590, 135, text="Father Name :", font=("veradana", 12), fill="Black")
mobile = canvas.create_text(1020, 135, text="Mobile Number:", font=("veradana", 12), fill="Black")
email = canvas.create_text(160, 190, text="email id : ", font=("veradana", 12), fill="Black")
marks = canvas.create_text(590, 190, text="10th Marks :", font=("veradana", 12), fill="Black")
school1 = canvas.create_text(1020, 190, text="10th School :", font=("veradana", 12), fill="Black")
school2 = canvas.create_text(150, 255, text="12th School :", font=("veradana", 12), fill="Black")
mark = canvas.create_text(590, 255, text="12th Marks :", font=("veradana", 12), fill="Black")
collage = canvas.create_text(1040, 255, text="Collage :", font=("veradana", 12), fill="Black")
password = canvas.create_text(150, 310, text="Password :", font=("veradana", 12), fill="Black")
password1 = canvas.create_text(570, 310, text="Conform Password :", font=("veradana", 12), fill="Black")
scurty = canvas.create_text(1015, 310, text="Security Question :", font=("veradana", 12), fill="Black")
scurtyans = canvas.create_text(1015, 360, text="Security Answer :", font=("veradana", 12), fill="Black")
# text for from end

# entry for from start
fistname = Entry(root, width=30, highlightthickness=2, textvariable=var_fname)
fistname_window = canvas.create_window(200, 70, anchor="nw", window=fistname)
midlname = Entry(root, width=30, highlightthickness=2, textvariable=var_mname)
midlname_window = canvas.create_window(650, 70, anchor="nw", window=midlname)
lastname = Entry(root, width=30, highlightthickness=2, textvariable=var_lname)
lastname_window = canvas.create_window(1080, 70, anchor="nw", window=lastname)
fathername = Entry(root, width=30, highlightthickness=2, textvariable=var_fathername)
fathername_window = canvas.create_window(650, 125, anchor="nw", window=fathername)
mobile1 = Entry(root, width=30, highlightthickness=2, textvariable=var_mobileno)
mobile1_window = canvas.create_window(1080, 125, anchor="nw", window=mobile1)
validate_contact = root.register(checkcontact)
mobile1.config(validate='key', validatecommand=(validate_contact, '%P'))
emailid = Entry(root, width=30, highlightthickness=2, textvariable=var_emailid)
emailid_window = canvas.create_window(200, 180, anchor="nw", window=emailid)
# validate_email = root.register(checkemail)
# emailid.config(validate='key', validatecommand=(validate_email, '%P'))
school3 = Entry(root, width=30, highlightthickness=2, textvariable=var_ten)
school3_window = canvas.create_window(650, 180, anchor="nw", window=school3)
mark1 = Entry(root, width=30, highlightthickness=2, textvariable=var_tenschool)
mark1_window = canvas.create_window(1080, 180, anchor="nw", window=mark1)
school4 = Entry(root, width=30, highlightthickness=2, textvariable=var_twelethschool)
school4_window = canvas.create_window(200, 245, anchor="nw", window=school4)
mark2 = Entry(root, width=30, highlightthickness=2, textvariable=var_tweleth)
mark2_window = canvas.create_window(650, 245, anchor="nw", window=mark2)
pswd = Entry(root, width=30, highlightthickness=2, textvariable=var_password)
pswd_window = canvas.create_window(200, 300, anchor="nw", window=pswd)
# validate_password = root.register(checkpassword)
# pswd.config(validate='key', validatecommand=(validate_password, '%P'))
pswd1 = Entry(root, width=30, highlightthickness=2, textvariable=var_confpawd)
pswd1_window = canvas.create_window(650, 300, anchor="nw", window=pswd1)
answer = Entry(root, width=30, highlightthickness=2, textvariable=var_answer)
answer_window = canvas.create_window(1080, 350, anchor="nw", window=answer)
# radiobutton
f = Radiobutton(root, value="Female", variable=var_gender)
m = Radiobutton(root, value="Male", variable=var_gender)
var_gender.set("Male")
f_window = canvas.create_window(200, 125, anchor="nw", window=f)
m_window = canvas.create_window(310, 125, anchor="nw", window=m)

# return ChkBtn
combo_collage = ttk.Combobox(root, font=("Times New Roman", 12, "bold"), state="readonly", justify='center',
                             textvariable=var_collage)
combo_collage["values"] = ("Select", "IIT kanpur", "IIT Roorkiee", "MIT", "Jaipjriya", "Amity", "Allen house", "JNU",
                           "NIT", "JSA", " R V Collage", "Other")
combo_collage_window = canvas.create_window(1080, 240, anchor="nw", window=combo_collage)
combo_collage.current(0)

security = ttk.Combobox(root, font=("Times New Roman", 12, "bold"), state="readonly", justify='center',
                        textvariable=var_security)
security["values"] = ("Select", "Your birth place", "Your mother name", "Your favourite place", "Your pet name")
security_window = canvas.create_window(1080, 300, anchor="nw", window=security)
security.current(0)
# check button
checkbutton = Checkbutton(root, text=" I Agree To All The Terms And Condition ", font=("times New Roman", 10),
                          onvalue=1, offvalue=0, variable=var_check)
checkbutton_window = canvas.create_window(280, 400, anchor="nw", window=checkbutton)
'''check_lbl = Label(checkbutton, text="Please Agree to term and condition", font=("times New Roman", 10), fg="red")
check_lbl_window = canvas.create_window(145, 350, anchor="nw", window=check_lbl)'''

# end buttons
submit = Button(root, text="Submit", fg="black", activebackground="black", command=submit1)
submit_window = canvas.create_window(650, 435, anchor="nw", window=submit)


root.mainloop()
