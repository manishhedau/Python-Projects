# creating the buttonss

from tkinter import *
 
root = Tk()

def myclick():
    label = Label(root,text="Hello i Am Manish !")
    label.pack()

button = Button(root,text = "Click Me",command = myclick,padx=30,pady=10,fg='#fff',bg='#000')
# we can change the size of the button by using padx,pady
# fg, change the color of the text in the button
# bg, change the button background colur 

# pack function pack the anything label or button middle of the screen
button.pack()

root.mainloop()