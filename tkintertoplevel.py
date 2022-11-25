from tkinter import *
root=Tk()
def open_window():
    top=Toplevel(root)
    btn3 = Button(top, text="close", bg="red", fg="white",
                  font=("Comic Sans Ms", 12, "bold"), command=top.destroy)
    btn3.pack()
    top.geometry("400x500+120+120")

btn=Button(root,text="toplevel",bg="red",fg="white",
           font=("Comic Sans Ms",12,"bold"),command=open_window)
btn.pack()

btn1=Button(root,text="close",bg="red",fg="white",
           font=("Comic Sans Ms",12,"bold"),command=quit)
btn1.pack()
root.geometry("400x500+120+120")
root.mainloop()