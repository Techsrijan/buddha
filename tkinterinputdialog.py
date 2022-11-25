from tkinter import *
from tkinter import simpledialog
root=Tk()
def add_marks():
    sum=0
    for i in range(5):
        a=simpledialog.askinteger(title="marks calculator",prompt="Enter Marks")
        sum=sum+a
    print(sum)
btn1=Button(root,text="Add Marks",bg="red",fg="white",
           font=("Comic Sans Ms",12,"bold"),command=add_marks)
btn1.pack()
root.geometry("400x500+120+120")
root.mainloop()