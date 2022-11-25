from tkinter import *
root=Tk()

def getdata():
    print(i.get())
    
lab=LabelFrame(root,text="Select Gender")
i=IntVar()
r=Radiobutton(lab,text="Male",value=1,variable=i)
r.pack()
r1=Radiobutton(lab,text="FeMale",value=2,variable=i)
r1.pack()
lab.pack()
j=IntVar()
r11=Radiobutton(root,text="OBC",value=1,variable=j)
r11.pack()
r12=Radiobutton(root,text="GENERAL",value=2,variable=j)
r12.pack()
btn1=Button(root,text="close",bg="red",fg="white",
           font=("Comic Sans Ms",12,"bold"),command=getdata)
btn1.pack()
root.geometry("400x500+120+120")
root.mainloop()