from tkinter import *

root = Tk()
root.title('Pizza Time')
#root.iconbitmap('')

pizza_frame = LabelFrame(root, padx=5, pady=5, text='Type of Pizza')
pizza_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

MODES = [
    ('Peperoni', 'Peperoni'),
    ('Chesse', 'Chesse'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Peperoni')

for text, mode in MODES:
    Radiobutton(pizza_frame, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(pizza_frame, text=value)
    myLabel.pack()


pizzaLabel = Label(pizza_frame, text=pizza.get())
pizzaButton = Button(pizza_frame, text='Click Here', command=lambda: clicked(pizza.get()))
pizzaButton.pack()
pizzaLabel.pack()

root.mainloop()