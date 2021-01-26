import pyautogui 
import time
import tkinter as tk

def ScreenShot():
    name = int(round(time.time()*1000))
    name = 'C:\\Users\HP\\Desktop\\20+ project\\project1\\screenshots\\{}.png'.format(name)
    time.sleep(1)
    img = pyautogui.screenshot(name)
    img.show()

# ScreenShot()
root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

f_button = tk.Button(
    frame,
    text = 'Take Screenshot',
    command = ScreenShot)
f_button.pack(side = tk.LEFT)

close = tk.Button(
    frame,
    text = 'Quit',
    command = quit)
close.pack(side = tk.LEFT)  

root.mainloop()