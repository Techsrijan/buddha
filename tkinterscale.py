from tkinter import *
from tkinter import simpledialog
root=Tk()
def getdata():
    print(s.get())
    print(sp.get())

s=Scale(root,from_=100,to=500,orient=HORIZONTAL,sliderlength=80,length=300,width=50)
s.set(200)
s.pack()

sp=Spinbox(root,from_=1,to=5)
sp.pack()
btn1=Button(root,text="Add Marks",bg="red",fg="white",
           font=("Comic Sans Ms",12,"bold"),command=getdata)
btn1.pack()
root.geometry("400x500+120+120")
root.mainloop()