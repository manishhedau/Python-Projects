from tkinter import *

root = Tk()
# window name
root.title("Calculator")

# entry box 
entry = Entry(root,width=40,borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=30)


def Button_click(number):
    # entry.delete(0,END)
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def Button_clear():
    entry.delete(0,END)

def Button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_number)
    entry.delete(0,END)

def Button_equal():
    second_number = entry.get()
    entry.delete(0,END)
    if math == "Addition":
        entry.insert(0,f_num+int(second_number))

    if math == "Subtaction":
        entry.insert(0,f_num-int(second_number))
    
    if math == "Multiply":
        entry.insert(0,f_num*int(second_number))
    
    if math == "Devide":
        entry.insert(0,f_num/int(second_number))

def Button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_number)
    entry.delete(0,END)

def Button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "Multiply"
    f_num = int(first_number)
    entry.delete(0,END)

def Button_devide():
    first_number = entry.get()
    global f_num
    global math
    math = "Devide"
    f_num = int(first_number)
    entry.delete(0,END)


button1 = Button(root,text="1",padx=40,pady=20,command=lambda:Button_click(1))
button2 = Button(root,text="2",padx=40,pady=20,command=lambda:Button_click(2))
button3 = Button(root,text="3",padx=40,pady=20,command=lambda:Button_click(3))
button4 = Button(root,text="4",padx=40,pady=20,command=lambda:Button_click(4))
button5 = Button(root,text="5",padx=40,pady=20,command=lambda:Button_click(5))
button6 = Button(root,text="6",padx=40,pady=20,command=lambda:Button_click(6))
button7 = Button(root,text="7",padx=40,pady=20,command=lambda:Button_click(7))
button8 = Button(root,text="8",padx=40,pady=20,command=lambda:Button_click(8))
button9 = Button(root,text="9",padx=40,pady=20,command=lambda:Button_click(9))
button0 = Button(root,text="0",padx=40,pady=20,command=lambda:Button_click(0))

button_add = Button(root,text="+",padx=39,pady=20,command=Button_add)
button_equal = Button(root,text="=",padx=87,pady=20,command=Button_equal)

button_clear = Button(root,text='Clear',padx=79,pady=20,command=Button_clear )



button_subtract = Button(root,text="-",padx=40,pady=20,command=Button_subtract)
button_multiply = Button(root,text="*",padx=42,pady=20,command=Button_multiply)

button_devide = Button(root,text='/',padx=42,pady=20,command=Button_devide)


# puts button on the screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0,columnspan=1)

# symbols grids
button_add.grid(row=5,column=0,columnspan=1)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)
button_subtract.grid(row=6,column=0,)
button_multiply.grid(row=6,column=1)
button_devide.grid(row=6,column=2)

root.mainloop()