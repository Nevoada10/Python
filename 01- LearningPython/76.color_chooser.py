# Import the tkinter library, which is used for creating GUI applications.
from tkinter import *

# Import the colorchooser submodule from tkinter, which provides a color selection dialog.
from tkinter import colorchooser


# Define a function called "click" that will be called when the button is clicked.
def click():
    # Open a color selection dialog and store the chosen color in the "color" variable.
    color = colorchooser.askcolor()

    # Print the selected color, which is a tuple containing RGB values and a hexadecimal representation.
    print(color)

    # Extract the hexadecimal color code from the tuple and store it in the "color_hex" variable.
    color_hex = color[1]  # For example: ((255, 0, 240), '#ff00f0')
    if color[1]:
        print(color_hex)  # Print the hexadecimal color code.
        window.config(bg=color_hex)  # Set the background color of the window.
    else:
        print("Color selection canceled")


window = Tk()  # Create a Tkinter window.
window.geometry("420x420")  # Set the size of the window to 420x420 pixels.
# Create a button with the label "click me" and set its command to call the "click" function when clicked.
button = Button(text="click me", command=click)

# Pack the button into the window so it becomes visible.
button.pack()

# Start the Tkinter main event loop, which listens for user interactions and updates the GUI.
window.mainloop()
