from tkinter import *

root=Tk()
canvas=Canvas(root,height=800,width=600,bg="white")
line=canvas.create_line(0,0,600,800,fill="red",width="5")
rectangle=canvas.create_rectangle(200,200,150,150,fill="blue")
rectangle=canvas.create_oval(200,200,150,120,fill="white")
canvas.pack()
root.geometry("800x600+120+120")
root.mainloop()
