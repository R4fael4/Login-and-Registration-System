from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

def forget_pass():
    def change_password():
        if user_entry.get() == '' or newpass_entry.get() =='' or confirmpass_entry.get() =='':
            messagebox.showerror('Error', 'All fields are required', parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Passwords do not match', parent=window)
        else:
            con = pymysql.connect(host='localhost',user='root',password='123', database='userdata')
            mycursor = con.cursor() 
            query = 'select * from data where username = %s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid username', parent=window)
            else:
                query = 'update data set password = %s where username = %s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password changed successfully', parent=window)
                window.destroy()
    
    window = Toplevel()
    window.title('Change Password')
    
    bgPic = ImageTk.PhotoImage(file = 'background.png')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading_label = Label(window, text='Reset Password', font=('Helvetica', 20, 'bold'), fg='black', bg='SlateBlue3')
    heading_label.place(x=780, y=170)

    user_label = Label(window, text='Username', font=('Helvetica', 11, 'bold'), fg='black', bg='SlateBlue3')
    user_label.place(x=750, y=240)
    Frame(window, width=300, height=2, bg='black').place(x=740, y=300)
    user_entry = Entry(window, width=30, font=('Helvetica', 11, 'bold'), bd=0, fg='black', bg='SlateBlue3')
    user_entry.place(x=750, y=270)

    newpass_label = Label(window, text='New Password', font=('Helvetica', 11, 'bold'), fg='black', bg='SlateBlue3')
    newpass_label.place(x=750, y=320)
    Frame(window, width=300, height=2, bg='black').place(x=740, y=380)
    newpass_entry = Entry(window, width=35, font=('Helvetica', 11, 'bold'), bd=0, fg='black', bg='SlateBlue3')
    newpass_entry.place(x=750, y=350)

    confirmpass_label = Label(window, text='Confirm Password', font=('Helvetica', 11, 'bold'), fg='black', bg='SlateBlue3')
    confirmpass_label.place(x=750, y=400)
    Frame(window, width=300, height=2, bg='black').place(x=740, y=460)
    confirmpass_entry = Entry(window, width=35, font=('Helvetica', 11, 'bold'), bd=0, fg='black', bg='SlateBlue3')
    confirmpass_entry.place(x=750, y=430)

    submitButton = Button(window, text='Submit',font=('Open Sans', 16, 'bold'), fg='white', bg='black', 
                    activeforeground='white', activebackground='black', bd=0, cursor='hand2', width=19, command=change_password)
    submitButton.place(x=760, y=500)

    window.mainloop()


def login_user():
    username = usernameEntry.get()
    password = passwordEntry.get()
    if username == 'Username' or password == 'Password' or username == '' or password == '':
        messagebox.showerror('Error', 'All fields are required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='9012@@#38tcpjbs2328@@')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database connection error. Please try again.')
            return
        
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username = %s and password = %s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Success', 'Login successful')


def signup_page():
    root.destroy()
    import signup

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def hide():
    eyeButton.config(image=hide_image)  
    passwordEntry.config(show='*')  
    eyeButton.config(command=show) 

def show():
    eyeButton.config(image=show_image)  
    passwordEntry.config(show='')  
    eyeButton.config(command=hide)  


root = Tk()
root.geometry('1366x768')
root.title('Sign in')
bgImage = ImageTk.PhotoImage(Image.open('bg.png'))

bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(root, text='sign in', font=('Helvetica', 20, 'bold'), fg='black', bg='white')
heading.place(x=840, y=170)

usernameEntry = Entry(root, width=25, font=('Helvetica', 11, 'bold'), bd=0, fg='black')
usernameEntry.place(x=750, y=240)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
Frame(root, width=300, height=2, bg='black').place(x=740, y=270)

passwordEntry = Entry(root, width=25, font=('Helvetica', 11, 'bold'), bd=0, fg='black')
passwordEntry.place(x=750, y=310)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
Frame(root, width=300, height=2, bg='black').place(x=740, y=340)


show_image = PhotoImage(file='show.png')
hide_image = PhotoImage(file='hide.png')

eyeButton = Button(root, image=hide_image, bd=0, bg='white', activebackground='white', cursor='hand2'
                   , command=show)
eyeButton.place(x=1010, y=310)


forgetButton = Button(root, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2'
                    ,font=('Helvetica', 10, 'bold'), fg='black',activeforeground='steelblue3',command=forget_pass)
forgetButton.place(x=920, y=360)


loginButton = Button(root, text='Login',font=('Open Sans', 16, 'bold'), fg='white', bg='black', 
                    activeforeground='white', activebackground='black', bd=0, cursor='hand2', width=19, command=login_user)
loginButton.place(x=760, y=400)


orLabel = Label(root, text='─────────  OR ───────── ', font=('Open Sans', 16, 'bold'), fg='black', bg='white')
orLabel.place(x=720, y=460)


facebook_Logo = PhotoImage(file='facebook.png')
fbLabel = Label(root, image=facebook_Logo, bg='white')
fbLabel.place(x=780, y=500)

google_Logo = PhotoImage(file='google.png')
gLabel = Label(root, image=google_Logo, bg='white')
gLabel.place(x=870, y=500)

twitter_Logo = PhotoImage(file='twitter.png')
tLabel = Label(root, image=twitter_Logo, bg='white')
tLabel.place(x=960, y=500)


signupLabel = Label(root, text=' Dont have an account? ', font=('Open Sans', 11, 'bold'), fg='black', bg='white')
signupLabel.place(x=740, y=560)

newaccountButton = Button(root, text='Create new one',font=('Open Sans', 11, 'bold underline'), fg='black', bg='white', 
                    activeforeground='steelblue3', activebackground='white', bd=0, cursor='hand2', command=signup_page)
newaccountButton.place(x=910, y=558)

root.mainloop()


