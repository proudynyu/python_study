# Simples calculator using Tkinter
# Learn from freecodecamp.org
# igor Becker
# 27/01/2020

from tkinter import *

# Basic of Tkinter program
root = Tk()
root.title('Simple Calculator')

# Input text
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def onClick(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    return

def onClear():
    e.delete(0, END)

def onAdd():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)


def onEqual():
    seconde_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(seconde_number))

# DEFINING --> Numeric Buttons
b1 = Button(root, text='1', padx=40, pady=20, command=lambda: onClick(1))
b2 = Button(root, text='2', padx=40, pady=20, command=lambda: onClick(2))
b3 = Button(root, text='3', padx=40, pady=20, command=lambda: onClick(3))
b4 = Button(root, text='4', padx=40, pady=20, command=lambda: onClick(4))
b5 = Button(root, text='5', padx=40, pady=20, command=lambda: onClick(5))
b6 = Button(root, text='6', padx=40, pady=20, command=lambda: onClick(6))
b7 = Button(root, text='7', padx=40, pady=20, command=lambda: onClick(7))
b8 = Button(root, text='8', padx=40, pady=20, command=lambda: onClick(8))
b9 = Button(root, text='9', padx=40, pady=20, command=lambda: onClick(9))
b0 = Button(root, text='0', padx=40, pady=20, command=lambda: onClick(0))

# DEFINING --> Text Button

bAdd = Button(root, text='+', padx=40, pady=20, command=lambda: onAdd())
bEqual = Button(root, text='=', padx=94, pady=20, command=onEqual)
bClear = Button(root, text="Clear", padx=84, pady=20, command=lambda: onClear())

# SCREEN --> Numeric buttons

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

bClear.grid(row=4, column=1, columnspan=2)
bAdd.grid(row=5, column=0)
bEqual.grid(row=5, column=1, columnspan=2)

# Main Loop
root.mainloop()