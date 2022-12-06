from tkinter import *
from tkinter import messagebox,ttk,filedialog
import pymysql



#print(h,w)

#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

############### database conncetion #########################
def dbconfig():
    global mycursor,conn
    conn = pymysql.connect(host="localhost", user="root", db="buddha")
    mycursor = conn.cursor()

##########main heading ##########
def mainheading():
    lable=Label(taz,text="                   HOTEL MANAGMENT SYSTEM                     ",bg='yellow',fg='red',
                font=("Comic Sans Ms",25,'bold'))
    lable.grid(row=0,column=0,columnspan=4)


###### login window##########

def loginwindow():
    global usernameVar,passwordVar
    usernameVar = StringVar()
    passwordVar = StringVar()
    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2)

########logout########
def logout():
    remove_all_widgets()
    mainheading()
    loginwindow()

########welcome window #######


def adminlogin():
    username = usernameVar.get()
    password = passwordVar.get()
    if username=='' or password=='':
        messagebox.showerror("Validation Error","Please Fill Both Values")
    else:
        dbconfig()
        que = "select * from login_info where binary userid=%s and binary password=%s"
        val = (username, password)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        flag = False
        for row in data:
            flag = True

        conn.close()
        if flag == True:
            welcomewindow()
        else:
            messagebox.showerror("Login Error", "Either User Name for Password is incorrect")
################

def welcomewindow():
    remove_all_widgets()
    mainheading()
    welcomeLabel = Label(taz, text="Welcome Window", font="Arial 30")
    welcomeLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)
    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=4, column=1, columnspan=2)

taz=Tk()
taz.title("Hotel Managment System")
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
taz.geometry("%dx%d+0+0"%(w,h))
taz.resizable(0,0)
mainheading()
loginwindow()
taz.mainloop()