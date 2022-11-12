from tkinter import *
root=Tk()

def left(event=''):
    print("left clcik")


btn=Button(root,text="Left",command=left)
btn.pack()

root.bind("<Control-c>",left)

#btn.bind("<Button-1>",left)
root.geometry("400x500+120+120")
root.mainloop()