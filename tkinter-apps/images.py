from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code')

# change image icon of the window
# --> root.iconbitmap('')

my_img = ImageTk.PhotoImage(Image.open('img_ex.png'))

my_label = Label(image=my_img)

my_label.pack()


# botao de sair
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
