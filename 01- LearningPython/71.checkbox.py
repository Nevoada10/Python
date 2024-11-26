from tkinter import *


def display():
    if x.get() == 1:
        print("You agree.")
    else:
        print("You disagree.")


window = Tk()
x = IntVar()  # BOOLEAN # STRING # INT
directory = "/Users/urielnevessilva/Desktop/background.png"
image = PhotoImage(file=directory)

check_button = Checkbutton(window,
                           text="I agree to ___",
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="red",  # These actually look to not work on Mac OS
                           activebackground="purple",  # These actually look to not work on Mac OS
                           padx=25,  # Checkbox distance in pixels from the text.
                           pady=10,  # Checkbox distance in pixels from the text.
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           image=image,
                           compound="left")

#   EXECUTION
check_button.pack()
window.mainloop()
