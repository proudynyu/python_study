from tkinter import *

root = Tk()
root.title('Frames')
#root.iconbitmap('sem_icone')

frame = LabelFrame(root, text='This is my frame', padx=10, pady=10)

b = Button(
    frame, 
    text="First button in Frame", 
)


frame.pack(padx=20, pady=20)
b.pack()

root.mainloop()