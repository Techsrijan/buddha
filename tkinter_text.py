from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("My First Window")
def getdata():
    c=text.get(1.0,END)
    print(c.find('the'))
def selecteddata():
    x=text.selection_get()
    print(x)

def cleartextbox():
    text.delete(1.0,END)

def get_select_pos():
    x = text.selection_get()
    loc=text.search(x,1.3,END)
    print(loc)

def insert_file_Data():
    f = filedialog.askopenfile(title="My open file", initialdir="/",
                                 filetypes=(("ALL FILES", "*.*"), ("TEXT FILES", "*.txt")))
    #f=open("hello.txt","r")
    for data in f:
        print(data)
        text.insert(INSERT,data)

def save_file_Data():
    c = text.get(1.0, END)
    f=open("hello.txt","w")
    f.write(c)
text=Text(root,selectbackground="grey",height=20,width=50,wrap=WORD)
#text.pack(fill=BOTH,expand=1)
text.insert(INSERT,"THIS ID")
text.pack()
btn=Button(root,text="getdata",bg="red",fg="white",
           font=("Comic Sans Ms",12,"bold"),command=getdata)
btn.pack()

btn1=Button(root,text="selecteddata",bg="red",fg="white",
           font=("Comic Sans Ms",20,"bold"),command=selecteddata)
btn1.pack(side=TOP) #to display the widget
# btn.pack(side=BOTTOM) #to display the widget
#
btn2=Button(root,text="cleartextbox",bg="red",fg="white",
           font=("Comic Sans Ms",20,"bold"),command=cleartextbox)
btn2.pack() #to display the widget
#
btn3=Button(root,text="getselecteditemposition",bg="red",fg="white",
           font=("Comic Sans Ms",20,"bold"),command=get_select_pos)
btn3.pack() #to display the widget
#
btn5=Button(root,text="insertfiledata",bg="red",fg="white",
           font=("Comic Sans Ms",20,"bold"),command=insert_file_Data)
btn5.pack() #to display the widget

btn6=Button(root,text="savefile",bg="red",fg="white",
           font=("Comic Sans Ms",20,"bold"),command=save_file_Data)
btn6.pack() #to display the widget
root.geometry("800x800+200+100") # to resize the window and location

root.wm_iconbitmap("notepad.ico")#icon
root.mainloop()