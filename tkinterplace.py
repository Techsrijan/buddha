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
label.place(x=50,y=100)
#x=IntVar()
x=StringVar()
ent=Entry(root,font=("Airel",15,'bold'),
          textvariable=x,justify='right',bd=5)
ent.place(y=100,x=300)


label1=Label(root,text="Enter Any number",bg="blue",
            fg='yellow',font=("Airel",15,'bold'))
label1.place(x=50,y=200)
#y=IntVar()
y=StringVar()
ent1=Entry(root,font=("Airel",15,'bold'),
          textvariable=y,justify='right',bd=5)
ent1.place(y=200,x=300)

btn=Button(root,text="ADD",font=("Airel",15,'bold'),bg="red",
           fg="yellow",command=getData)
btn.place(y=300,x=260)

z=StringVar()
result=Label(root,
            fg='black',font=("Airel",15,'bold'),textvariable=z)
result.place(x=260,y=400)
root.geometry("600x500+120+120")
root.mainloop()