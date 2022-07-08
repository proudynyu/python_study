# Using Tkinter to create user interface
# Igor Becker - 27/01/2020

# defining a input box

from tkinter import *

# Base of a Tkinter program, must come first as anything
root = Tk()

e = Entry(
    root, 
    width=50, 
    fg="blue",
    borderwidth=5)

e.pack()

def get_button():
    labelButtom = Label(root, text=e.get())
    labelButtom.pack()

name_buttom = Button(root, text="Enter your name", command=get_button)

name_buttom.pack()
# main Loop for the program run
root.mainloop()
