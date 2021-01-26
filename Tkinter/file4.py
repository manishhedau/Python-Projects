from tkinter import *

root = Tk()

label = Label(root,text= "Enter your Name ?")
label.grid(row=0,column=0)


entry = Entry(root,width=20)
entry.grid(row=0,column=1)
# by default text into input box so we used insert 
entry.insert(0,"Enter your Name :")

def clickme():
    mylabel = Label(root,text='Hello '+entry.get(),fg='Green',padx=20,pady=50)
    mylabel.grid(row=2,column=2)


button = Button(root,text="click me",command=clickme)
button.grid(row=1,column=0)
root.mainloop()