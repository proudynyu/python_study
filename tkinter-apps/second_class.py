# Using Tkinter to create user interface
# Igor Becker - 27/01/2020

# Tk is a grid program that uses columns and rows
# To define the position of something, must know this

from tkinter import *

# Base of a Tkinter program, must come first as anything
root = Tk()

# define a thing a put it in the screen

# DEFINING
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Hello Igor")

# SCREEN (using GRID)

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# main Loop for the program run
root.mainloop()
