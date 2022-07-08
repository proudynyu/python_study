from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title( 'Image Viewer' )

# acessar imagens
my_img1 = ImageTk.PhotoImage( Image.open( 'images/img_1.jpg' ) )
my_img2 = ImageTk.PhotoImage( Image.open( 'images/img_2.jpg' ) )
my_img3 = ImageTk.PhotoImage( Image.open( 'images/img_3.jpg' ) )
my_img4 = ImageTk.PhotoImage( Image.open( 'images/img_4.jpg' ) )

img_list = [my_img1, my_img2, my_img3, my_img4]


my_label = Label( image=my_img1 )
my_label.grid( row=0, column=0, columnspan=3 )

str_status = f'image 1 of {str(len(img_list))}'
status = Label(root, text=str_status, bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# funcoes
def fowardImg( img_num ):
    global my_label
    global button_foward
    global button_back

    if img_num == len(img_list)+1:
        button_foward = Button( root, text='>>', state=DISABLED)

    else:
        my_label.grid_forget()
        my_label = Label( image=img_list[ img_num - 1 ] )    
        button_foward = Button( root, text=">>", command=lambda: fowardImg( img_num + 1 ) )
        button_back = Button( root, text='<<', command=lambda: backImg( img_num - 1 ) )    
        my_label.grid( row=0, column=0, columnspan=3 )
        button_foward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)
        
        # UPDATE THE STATUS BAR
        str_status = f'image {img_num} of {str(len(img_list))}'
        status = Label(root, text=str_status, bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def backImg( img_num ):
    global my_label
    global button_foward
    global button_back

    if img_num == 0:
        button_foward = Button( root, text='>>', state=DISABLED)

    else:
        my_label.grid_forget()
        my_label = Label( image=img_list[ img_num - 1 ] )    
        button_foward = Button( root, text=">>", command=lambda: fowardImg( img_num + 1 ) )
        button_back = Button( root, text='<<', command=lambda: backImg( img_num - 1 ) )
        my_label.grid( row=0, column=0, columnspan=3 )
        button_foward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)

        # UPDATE THE STATUS BAR
        str_status = f'image {img_num} of {str(len(img_list))}'
        status = Label(root, text=str_status, bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Control buttons
button_back = Button( root, text="<<", command=backImg, state=DISABLED )
button_foward = Button( root, text=">>", command=lambda: fowardImg(2) )
button_quit = Button(root, text="Exit Program", command=root.quit)

# button screen
button_back.grid(row=1, column=0)
button_foward.grid(row=1, column=2, pady=10)
button_quit.grid(row=1, column=1)

root.mainloop()
