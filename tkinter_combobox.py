from tkinter import *
from tkinter import ttk
def msg():
    print(c.get())
root=Tk()
l=[1,2,3,4,5,6,7,8,9,10,11,12]
c=ttk.Combobox(root,value=l)
c.set("Select Month")
c.pack()
btn=Button(root,text="Getdata",command=msg)
btn.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()
