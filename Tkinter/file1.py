# creating the label

from tkinter import *
 
root = Tk()

# creating a label widget
mylabel = Label(root,text='Hello World').grid(row = 0,column=0)
mylabel2 = Label(root,text = 'Hii I am Manish Hedau').grid(row=1,column = 0)

# showing it onto the screen
# mylabel.pack(50)


# we can also do like this
# mylabel.grid(row = 0,column=0)
# mylabel2.grid(row=1,column = 0)


root.mainloop()