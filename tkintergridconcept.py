from tkinter import *
root=Tk()
def getData():
    c=float(x.get())+float(y.get())
    print(c)
    z.set(c)
    x.set('')
    y.set('')


label=Label(root,text="Enter Any number",bg="blue",
            fg='yellow',font=("Airel",15,'bold'))
label.grid(row=0,column=0)
#x=IntVar()
x=StringVar()
ent=Entry(root,font=("Airel",15,'bold'),
          textvariable=x,justify='right',bd=5)
ent.grid(row=0,column=1)


label1=Label(root,text="Enter Any number",bg="blue",
            fg='yellow',font=("Airel",15,'bold'))
label1.grid(row=1,column=0)
#y=IntVar()
y=StringVar()
ent1=Entry(root,font=("Airel",15,'bold'),
          textvariable=y,justify='right',bd=5)
ent1.grid(row=1,column=1)

btn=Button(root,text="ADD",font=("Airel",15,'bold'),bg="red",
           fg="yellow",command=getData)
btn.grid(row=2,column=0,columnspan=2)

z=StringVar()
result=Label(root,
            fg='black',font=("Airel",15,'bold'),textvariable=z)
result.grid(row=7,column=0,columnspan=2)
#root.geometry("600x500+120+120")
root.mainloop()