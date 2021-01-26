from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Button object")


def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")




Button = Button(root,text='manish hedau',font=10,height=1,state=ACTIVE,fg='Blue'
                ,width=20,underline=-7,command=helloCallBack,bd=2,activebackground='Green',activeforeground='Red',justify=CENTER,relief=RIDGE)
Button.pack()

root.mainloop()