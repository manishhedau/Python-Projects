from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Button object")

first_name = Label(root,text='First Name :')
first_name.grid(row=0,column=0)
first_name_entry = Entry(root,justify=CENTER)
first_name_entry.grid(row=0,column=1)


last_name = Label(root,text='Last Name :')
last_name.grid(row=1,column=0)
last_name_entry = Entry(root,justify=CENTER)
last_name_entry.grid(row=1,column=1)

father_name = Label(root,text='Father Name :')
father_name.grid(row=2,column=0)
father_name_entry = Entry(root,justify=CENTER)
father_name_entry.grid(row=2,column=1)

mother_name = Label(root,text='Mother Name :')
mother_name.grid(row=3,column=0)
mother_name_entry = Entry(root,justify=CENTER)
mother_name_entry.grid(row=3,column=1)


phone_number = Label(root,text='Phone Number :')
phone_number.grid(row=4,column=0)
phone_number_entry = Entry(root,justify=CENTER)
phone_number_entry.grid(row=4,column=1)

email_id = Label(root,text='Email Id :')
email_id.grid(row=5,column=0)
email_id_entry = Entry(root,justify=CENTER)
email_id_entry.grid(row=5,column=1)

password = Label(root,text='Password :')
password.grid(row=6,column=0)
password_entry = Entry(root,justify=CENTER,show="*")
password_entry.grid(row=6,column=1)


def Submitinfo():
    msg = messagebox.showinfo( "User Details", "Your Information has successfully submited")
    lst=[first_name_entry,last_name_entry,father_name_entry,mother_name_entry,phone_number_entry,email_id_entry,password_entry]
    for i in lst:
        i.delete(0,END)

submit = Button(root,text='Submit',command=Submitinfo,height=1,font=5)
submit.grid(row=7,column=1)

root.mainloop()