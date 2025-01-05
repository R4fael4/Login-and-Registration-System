from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)


def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Passwords do not match')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please agree to the Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='123')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database connection error. Please try again.')
            return
        
        try:
           query = 'create database'
           mycursor.execute(query)
           query = 'use userdata'
           mycursor.execute(query)
           query = '(create table data (id int auto_increment primary key not null, email varchar(50), username varchar (50), password varchar(50))'
           mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
            
        query = 'select * from data where username = %s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exists')
        
        else:
            query='insert into data (email, username, password) values (%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Account created successfully')
            clear()
            signup_window.destroy()
            import signin

    
def login_page():
    signup_window.destroy()
    import signin

signup_window = Tk()    
signup_window.title('Sign up')

check = IntVar()

background = ImageTk.PhotoImage(Image.open('bg2.png'))
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

heading = Label(signup_window, text='Create an account', font=('Helvetica', 20, 'bold'), fg='black', bg='coral')
heading.place(x=770, y=170)

emailLabel = Label (signup_window, text='Email', font=('Helvetica', 10, 'bold'), fg='black', bg='coral')
emailLabel.place(x=750, y=230)
Frame(signup_window, width=300, height=2, bg='black').place(x=740, y=270)
emailEntry = Entry(signup_window, width=30, font=('Helvetica', 11, 'bold'), bd=0, fg='black', bg='coral')
emailEntry.place(x=760, y=250)

usernameLabel = Label (signup_window, text='Username', font=('Helvetica', 10, 'bold'), fg='black', bg='coral')
usernameLabel.place(x=750, y=280)
Frame(signup_window, width=300, height=2, bg='black').place(x=740, y=320)
usernameEntry = Entry(signup_window, width=30, font=('Helvetica', 11, 'bold'), bd=0, fg='black', bg='coral')
usernameEntry.place(x=760, y=300)

passwordLabel = Label (signup_window, text='Password', font=('Helvetica', 10, 'bold'), fg='black', bg='coral')
passwordLabel.place(x=750, y=330)
Frame(signup_window, width=300, height=2, bg='black').place(x=740, y=370)
passwordEntry = Entry(signup_window, width=30, font=('Helvetica', 11, 'bold'),bd=0, fg='black', bg='coral')
passwordEntry.place(x=760, y=350)

confirmLabel = Label (signup_window, text='Confirm Password', font=('Helvetica', 10, 'bold'), fg='black', bg='coral')
confirmLabel.place(x=750, y=380)
Frame(signup_window, width=300, height=2, bg='black').place(x=740, y=420)
confirmEntry = Entry(signup_window, width=30, font=('Helvetica', 11, 'bold'),bd=0, fg='black', bg='coral')
confirmEntry.place(x=760, y=400)

termsandconditions = Checkbutton(signup_window, text='I agree to the Terms & Conditions', font=('Helvetica', 10, 'bold'), fg='black', bg='coral', activebackground='white', cursor='hand2', variable=check)
termsandconditions.place(x=750, y=440)

signup_Button = Button(signup_window, text='Sign up', font=('Open Sans', 15, 'bold'), bd=0, fg='white', bg='black', activebackground='grey', activeforeground='white', width=15, command=connect_database) 
signup_Button.place(x=790, y=480)

alreadyaccount = Label(signup_window, text='Already have an account?', font=('Helvetica', 10, 'bold'), fg='black', bg='coral')
alreadyaccount.place(x=760, y=530)

login_Button = Button(signup_window, text='Login', font=('Open Sans', 12,'bold underline'), bd=0, fg='white', bg='coral',cursor='hand2', activebackground='coral', activeforeground='white', command=login_page)
login_Button.place(x=940, y=526)


signup_window.mainloop()