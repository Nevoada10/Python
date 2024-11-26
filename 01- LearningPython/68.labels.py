# label = an area widget that holds text and/or an image within a window

from tkinter import *
import os

directory = "/Users/urielnevessilva/Desktop/background.png"  # It just worked with PNG.

if os.path.isfile(directory):
    print(True)

# widgets = GUI elements: buttons, textbox, labels, images
# windows = serves as a container to hold or contain these widgets I

window = Tk()  # Uppercase T # Parenthesis = Construct
image = PhotoImage(file=directory)  # File
# Instantiate an instance of a window
label = Label(window,  # Instantiate an instance of a label  # ( Container/ Master )
              image=image,  # Location of the image relative to the text.
              compound="bottom",
              text="Hello World",
              font=("Arial", 40),
              fg="#00FF00",  # Font ground, color.
              bg="black",  # Background color # Already black by default on Mac OS
              # relief=SUNKEN,    # RAISED # SUNKEN  # Border style.
              bd=10,  # Bd = border width
              padx=20,  # Pad_x = Space between text and the border in the X axis.
              pady=20,  # Pad_x = Space between text and the border in the Y axis.
              )

window.geometry("1920x1080")  # Pass width and height.
window.title("First GUI program")

window.config(background="#5cfcff")  # Name of color # or Hexadecimal color.
# Fg = foreground = color of the font.

# name if it's in folder # Else: directory.
# converts photo into photo image format for tkinter.

label.pack()  # Place a label in the container. # By default is at the top center.
# label.place(x=100,y=100) # Place a label in the container in the desired position.
window.mainloop()  # Place window on computer screen, listen for events.
