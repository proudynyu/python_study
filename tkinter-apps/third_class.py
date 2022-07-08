# Using Tkinter to create user interface
# Igor Becker - 27/01/2020

# defining a button

from tkinter import *

# Base of a Tkinter program, must come first as anything
root = Tk()

def myClick():
    myLabel = Label(root, text="Whatever")
    myLabel.pack()

# DEFINING BUTTON
myButton = Button(
    root, 
    text="Click Me", 
    padx=50,
    pady=5, 
    command=myClick, 
    fg="red", 
    bg="blue")

# SCREEN (using GRID)
myButton.pack()


# main Loop for the program run
root.mainloop()
