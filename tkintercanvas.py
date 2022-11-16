from tkinter import *

root=Tk()
canvas=Canvas(root,height=800,width=600,bg="white")
# line=canvas.create_line(0,0,600,800,fill="red",width="5")
# rectangle=canvas.create_rectangle(200,200,300,350,fill="blue")
# rectangle=canvas.create_oval(200,200,300,350,fill="white")
# point=[200,110,480,200,280,280,200,110]
# poly=canvas.create_polygon(point,fill="green")
# #text=canvas.create_text("rohan")
# arc=canvas.create_arc(100,100,300,300,fill="orange",outline="white",extent=-180)

filename = PhotoImage(file = "best.gif")
image = canvas.create_image(200, 200, anchor=NW, image=filename)
canvas.pack()
canvas.pack()
root.geometry("800x600+120+120")
root.mainloop()
