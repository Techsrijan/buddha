from tkinter import *
from tkinter import ttk
def msg():
    c = l.curselection()
    print(c)
    for item in c:
        print(l.get(item))
def deldata():
    c = l.curselection()
    print(c)
    for item in c:
        print(l.delete(item))

# def cleardata():
#     l.clear()
root=Tk()
fr=Frame(root)
scroll=Scrollbar(fr)
# BROWSE SINGLE MULTIPLE EXTENDED
l=Listbox(fr,selectmode=EXTENDED,height=12,yscrollcommand=scroll.set)
for i in range(20):
    l.insert(i,i)
l.pack(side=LEFT)
scroll.config(command=l.yview)
scroll.pack(side=RIGHT,fill=Y)
fr.pack()
btn=Button(root,text="Getdata",command=msg)
btn.pack()
btn1=Button(root,text="Delete",command=deldata)
btn1.pack()
# btn3=Button(root,text="Clear",command=cleardata)
# btn3.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()
