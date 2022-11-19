from tkinter import *
root=Tk()
root.title("My First Window")
def getdata():
    print(text.get(1.5,END))

text=Text(root,selectbackground="grey")
#text.pack(fill=BOTH,expand=1)
text.insert(INSERT,"THIS ID")
text.pack()
btn=Button(root,text="getdata",bg="red",fg="white",
           font=("Comic Sans Ms",12,"bold"),command=getdata)
btn.pack()

# btn1=Button(root,text="Subtract",bg="red",fg="white",
#            font=("Comic Sans Ms",20,"bold"))
# btn1.pack(side=TOP) #to display the widget
# btn.pack(side=BOTTOM) #to display the widget
#
# btn2=Button(root,text="login",bg="red",fg="white",
#            font=("Comic Sans Ms",20,"bold"))
# btn2.pack(side=LEFT,fill=Y) #to display the widget
#
# btn3=Button(root,text="login4",bg="red",fg="white",
#            font=("Comic Sans Ms",20,"bold"))
# btn3.pack(side=RIGHT) #to display the widget
#
# btn5=Button(root,text="login5",bg="red",fg="white",
#            font=("Comic Sans Ms",20,"bold")).pack()
#btn5.pack() #to display the widget
root.geometry("800x800+200+100") # to resize the window and location

root.wm_iconbitmap("notepad.ico")#icon
root.mainloop()