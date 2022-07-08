from tkinter import *
import sqlite3

root = Tk()
root.title('Database')
root.geometry('420x500')

def addDb():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES(:first_name, :last_name, :city_name, :state_name, :zipcode)",

        {
            'first_name': first_entry.get(),
            'last_name': last_entry.get(),
            'city_name': city_entry.get(),
            'state_name': state_entry.get(),
            'zipcode': zipcode_entry.get()
        })

    conn.commit()
    conn.close()

    # CLEAR THE ENTRY BOXES
    first_entry.delete(0, END)
    last_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

def showDb():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' \t' + str(record[5]) + '\n'

    query_print = Label(root, text=print_records)
    query_print.grid(row=10, column=0, columnspan=2)
    conn.commit()
    conn.close()
    pass

def deleteDb():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    id_select = selector_entry.get()

    c.execute('DELETE from addresses WHERE oid=' + id_select)

    conn.commit()
    conn.close()
    pass

def editDb():
    top = Toplevel()
    top.title('Edit Panel')
    top.geometry('420x500')

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    edit_id_label = Label(top, text='ID')
    edit_id_entry = Entry(top, width=50)
    edit_id_label.grid(row=0, column=0, padx=10, pady=10)
    edit_id_entry.grid(row=0, column=1, padx=10, pady=10)

    first_name_edit = Label(top, text='First name')
    last_name_edit = Label(top, text='Last name')
    city_name_edit = Label(top, text='City name')
    state_name_edit = Label(top, text='State name')
    zipcode_edit = Label(top, text='Zipcode')

    # ENTRIES OF LABELS
    first_entry_edit = Entry(top, width=50)
    last_entry_edit = Entry(top, width=50)
    city_entry_edit = Entry(top, width=50)
    state_entry_edit = Entry(top, width=50)
    zipcode_entry_edit = Entry(top, width=50)

    # GRID DEFINING
    # LABELS GRID
    first_name_edit.grid(row=1, column=0, padx=10)
    last_name_edit.grid(row=2, column=0, padx=10)
    city_name_edit.grid(row=3, column=0, padx=10)
    state_name_edit.grid(row=4, column=0, padx=10)
    zipcode_edit.grid(row=5, column=0, padx=10)

    #ENTRY GRID
    first_entry_edit.grid(row=1, column=1)
    last_entry_edit.grid(row=2, column=1)
    city_entry_edit.grid(row=3, column=1)
    state_entry_edit.grid(row=4, column=1)
    zipcode_entry_edit.grid(row=5, column=1)

    conn.commit()
    conn.close()

def createDb():
    # CREATE INITIAL DATABASE
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE addresses (
        first_name text,
        last_name text,
        city_name text,
        state_name text,
        zipcode integer
    )''')
    conn.commit()
    conn.close()

#createDb()

# LABELS NAME
first_name = Label(root, text='First name')
last_name = Label(root, text='Last name')
city_name = Label(root, text='City name')
state_name = Label(root, text='State name')
zipcode = Label(root, text='Zipcode')

# ENTRIES OF LABELS
first_entry = Entry(root, width=50)
last_entry = Entry(root, width=50)
city_entry = Entry(root, width=50)
state_entry = Entry(root, width=50)
zipcode_entry = Entry(root, width=50)

# GRID DEFINING
# LABELS GRID
first_name.grid(row=0, column=0, padx=10)
last_name.grid(row=1, column=0, padx=10)
city_name.grid(row=2, column=0, padx=10)
state_name.grid(row=3, column=0, padx=10)
zipcode.grid(row=4, column=0, padx=10)

#ENTRY GRID
first_entry.grid(row=0, column=1)
last_entry.grid(row=1, column=1)
city_entry.grid(row=2, column=1)
state_entry.grid(row=3, column=1)
zipcode_entry.grid(row=4, column=1)

# Buttons
addButton = Button(root, text="Add Record to Database", command=addDb)
addButton.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

showButton = Button(root, text="Show Records", command=showDb)
showButton.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=157)

# DELETE RECORD
selector_id_label = Label(root, text='Selector ID')
selector_entry = Entry(root, width=50)

selector_id_label.grid(row=7, column=0, padx=10, pady=10)
selector_entry.grid(row=7, column=1)

delete_btn = Button(root, text='Delete Record', command=deleteDb)
delete_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=157)

# EDIT RECORD
edit_btn = Button(root, text='Edit Record', command=editDb)
edit_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=163)

root.mainloop()