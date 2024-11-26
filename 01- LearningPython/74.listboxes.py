# listbox = A listing of selectable text items within it's own container

from tkinter import *


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You ordered:")
    for index in food:
        print(index)
    # print("You ordered:", listbox.get(listbox.curselection()))
    # Using the current selection.


def add():
    listbox.insert(listbox.size() + 1, entry_box.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):  # Deleting, starting from
        listbox.delete(listbox.curselection())  # Backwards
        listbox.config(height=listbox.size())


window = Tk()

# Defining the widgets of the window.

listbox = Listbox(window,
                  font=("Constancia", 35),
                  width=12,
                  fg="Black",
                  bg="Grey",
                  selectmode=MULTIPLE)

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")
listbox.config(height=listbox.size())

submit_button = Button(window,
                       text="Submit",
                       command=submit,
                       )

add_button = Button(window,
                    text="Add",
                    command=add
                    )

delete_button = Button(window,
                       text="Delete",
                       command=delete
                       )

entry_box = Entry(window)

# Displaying the window with all of your widgets

entry_box.pack()
listbox.pack()  # Or place.
submit_button.pack()
add_button.pack()
delete_button.pack()
window.mainloop()
