from tkinter import *


# entry widget = textbox that accepts a single line of user input.

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 30),
              fg="#00FF00",
              bg="black",
              #  state=NORMAL,
              show="*"  # For passwords for example.
              )

submit_button = Button(window,
                       text="Submit",
                       command=submit,
                       )
delete_button = Button(window,
                       text="Delete",
                       command=delete,
                       )
backspace_button = Button(window,
                          text="Backspace",
                          command=backspace,
                          )
entry.insert(0, "Spongebob Squarepants")
entry.pack(side=LEFT)
submit_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
backspace_button.pack(side=LEFT)

window.mainloop()
