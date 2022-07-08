from tkinter import *

root = Tk()
root.title('Frames')
#root.iconbitmap('sem_icon')

frame = LabelFrame(root, padx = 10, pady = 10, text = "Circle in Frame")

frame.grid(row = 0, column = 0, padx = 5, pady = 5)

state = IntVar()

b1 = Radiobutton(frame, text = "First!", variable = state, value = 1)

b2 = Radiobutton(frame, text = 'Second!', variable = state, value = 2)

b3 = Radiobutton(frame, text = 'Third!', variable = state, value = 3)

b1.grid(row = 0, column = 0)

b2.grid(row = 1, column = 0)

b3.grid(row = 2, column = 0)

root.mainloop()