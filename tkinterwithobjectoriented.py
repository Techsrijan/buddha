from tkinter import *

class Myindow:
    def msg(self):
        print("hi")
    def __init__(self,window):
        self.btn=Button(window,text="open",command=self.msg)
        self.btn.pack()

root=Tk()
win=Myindow(root)
root.mainloop()