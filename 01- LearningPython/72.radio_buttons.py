# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *


def choice():
    print("You choose {} over the other options".format(food[x.get()]))
    pass


food = ["pizza", "hamburger", "hotdog"]

window = Tk()

x = IntVar()
directory = "/Users/urielnevessilva/Desktop/background.png"

Pizza_Image = PhotoImage(file=directory)
Hamburger_Image = PhotoImage(file=directory)
Hotdog_Image = PhotoImage(file=directory)
List_Images = [Pizza_Image, Hamburger_Image, Hotdog_Image]

for index in range(len(food)):
    radio_button = Radiobutton(window,  # Instantiate/create a radio button inside the window container.
                               text=food[index],  # Adds text to our radio buttons.
                               variable=x,  # Groups radio buttons together # ON or OFF
                               value=index,  # Assigns each radio button to a different value.
                               padx=25,  # Adds space between radio buttons and text in the x-axis.
                               font=("impact", 30),  # Changes the type and size of the font used.
                               image=List_Images[index],  # Adds each image to the corresponding object.
                               compound="left",  # Moves image to the left side of the text.
                               indicatoron=False,  # Removes circle indicators. # A.K.A PUSH BUTTONS.
                               width=375,
                               command=choice,
                               )  # Sets the width of buttons to 375 pixels

    radio_button.pack(anchor=W)  # Aligns radio buttons in the desired direction # W = West.

window.mainloop()
