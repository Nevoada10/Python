# text widget.
from tkinter import *


def submit():
    input = text.get("1.0", END)  # Collumn and Line
    print(input)


window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 10),  # Changes the size of the window also.
            height=8,
            width=20,  # Affects the size too.
            padx=20,
            pady=20,
            fg="Purple")

button = Button(window,
                text="Submit text:",
                command=submit)
text.pack()
button.pack()
window.mainloop()
