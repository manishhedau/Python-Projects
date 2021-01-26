# creating the input box/entry box

from tkinter import *
 
root = Tk()

label = Label(root, text = "Enter your name ? ")
label.pack()

Entry = Entry(root,width = 50,borderwidth=10,fg='Blue',bg='#fff')
# we can change the size of input box - width
# we can change the backgrund color
# also forground color. means text color
# we can also change  borderwidth
Entry.pack()
# get the user input
Entry.get()

label2 = Label(root,text="Hello"+Entry.get())
label2.pack()


root.mainloop()