from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Messages')
#root.iconbitmap(''),

# Pops a message in the screen
def popup():
    response = messagebox.askokcancel('First popup', 'Hello World')
    #Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked OK!").pack()
    else:
        Label(root, text='You clicked Cancel!').pack()

Button(root, text='Popup', command=popup).pack()

root.mainloop()