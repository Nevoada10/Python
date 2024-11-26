from tkinter import *

count = 0


def click():
    global count
    count = count + 1
    print("You clicked the button", count, "times.")


window = Tk()

directory = "/Users/urielnevessilva/Desktop/background.png"

icon = PhotoImage(file=directory)

button = Button(window,
                text="Click Me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",  # Light Green.
                bg="#000000",
                activeforeground="#00FF00",
                activebackground="#000000",
                state=ACTIVE,  # DISABLED OR ACTIVE # default = active.
                image=icon,
                compound="bottom"
                )

button.pack()

window.mainloop()
