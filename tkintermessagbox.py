from tkinter import *
from tkinter import messagebox
root=Tk()
def test():
    result=messagebox.showinfo(title="Question Box",message="Do you want to play this Game?")
    print(result)
    if result==True:
        print("Khelo")
    else:
        print("Bhago")

btn=Button(root,text="message box testing",command=test)
btn.pack()
root.geometry("500x600+120+120")
root.mainloop()