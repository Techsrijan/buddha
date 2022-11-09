from tkinter import *
root=Tk()
root.title("My First Window")
def msg():
    print("hi")
btn=Button(root,text="Add....",bg="red",fg="white",
           font=("Comic Sans Ms",20,"bold"),command=msg)
btn.pack() #to display the widget
root.geometry("400x500+200+100") # to resize the window and location
root.resizable(0,0) #user resizate tru or false
root.wm_iconbitmap("notepad.ico")#icon
root.mainloop()