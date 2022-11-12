from tkinter import *
root=Tk()

def left(event):
    print("left clcik")

def middle(event):
    print("middle click")

def right(event):
    print("right click")


btn=Button(root,text="Left")
btn.pack()

btn1=Button(root,text="middle")
btn1.pack()

btn2=Button(root,text="Right")
btn2.pack()

btn.bind("<Button-1>",left)
btn1.bind("<Button-2>",middle)
btn2.bind("<Button-3>",right)
root.geometry("400x500+120+120")
root.mainloop()