# Using Tkinter to create user interface
# Igor Becker - 27/01/2020

from tkinter import *

# Base of a Tkinter program, must come first as anything
root = Tk()

# define a thing a put it in the screen

# DEFINING
myLabel = Label(root, text="Hello World!")

# SCREEN (Packing on the screen, not the best method)
myLabel.pack()

# main Loop for the program run
root.mainloop()
