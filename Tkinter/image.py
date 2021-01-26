from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("My Application ")
root.iconbitmap(r'C:\Users\HP\Downloads\Logo.png')

my_img = ImageTk.PhotoImage(Image.open(r'C:\Users\HP\Downloads\cv-template-06.jpg'))

label = Label(image=my_img)
label.grid(row=0,column=0,columnspan=3)

def Button_quit():
    exit()

button_quit = Button(root,text ="Exit Program ",command=Button_quit)
button_quit.grid(row=1,column=0)
root.mainloop()