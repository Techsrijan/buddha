from tkinter import *
from tkinter import filedialog
def msg():
    res=filedialog.askopenfile(title="My open file",initialdir="/",
                       filetypes=(("ALL FILES","*.*"),("TEXT FILES","*.txt")))
    print(res)

root=Tk()


btn=Button(root,text="openfile",command=msg)
btn.pack()
# btn1=Button(root,text="Delete",command=deldata)
# btn1.pack()
# btn3=Button(root,text="Clear",command=cleardata)
# btn3.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()
