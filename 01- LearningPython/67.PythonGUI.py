from tkinter import *
import os

# widgets = GUI elements: buttons, textbox, labels, images
# windows = serves as a container to hold or contain these widgets I
directory = "/Users/urielnevessilva/Desktop/background.png" # It just worked with PNG.

if os.path.isfile(directory):
    print(True)

window = Tk()  # Uppercase T # Parenthesis = Construct
# Instantiate an instance of a window
window.geometry("420x420")  # Pass width and height.
window.title("First GUI program")
window.config(background="#5cfcff")  # Name of color # or Hexadecimal color.
icon = PhotoImage(directory)  # File
window.iconphoto(True,icon)
# name if it's in folder # Else: directory.
# converts photo into photo image format for tkinter.


window.mainloop()  # Place window on computer screen, listen for events.
