from tkinter import *
root=Tk()

def msg(event=""):
    print("hi")
main_menu=Menu(root)

root.config(menu=main_menu)
root.bind("<Alt-c>",msg)
#creating filemenu
fileMenu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=msg, accelerator="Alt+Enter")
fileMenu.add_separator()
fileMenu.add_command(label="Save",  accelerator="Ctrl+S")

fileMenu.add_command(label="Exit",command=quit)
# add a submenu
sub_menu = Menu(fileMenu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')
# add the File menu to the menubar
fileMenu.add_cascade(label="Preferences",menu=sub_menu)

#creating Editmenu
editMenu=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut")
root.geometry("500x600+120+120")
root.mainloop()