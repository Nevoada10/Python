from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="This is an info message box.",
    #                   message="in the bottle")

    # while True:
    #   messagebox.showwarning(title="This is an info message box.",
    #                          message="VIRUS DETECTED")

    # messagebox.showerror(title="Error", message= "Something went wrong")

    # if messagebox.askokcancel(title="Ask ok cancel", message="Do you want to do it?"):
    #     print("You did it!")
    # else:
    #    print("You didn't it.")

    # if messagebox.askretrycancel(title="ask retry cancel", message="Do you want to retry it?"):
    #    print("You did retry it!")
    # else:
    #    print("You didn't retry it.")

    # if messagebox.askyesno(title="Ask Yes or No", message="Do you like cake?"):
    # print("I don't like cake but you do.")
    # else:
    # print("You don't like cake, neither do I.")

    # answer = messagebox.askquestion(title="Question", message="What do you think?")
    # if answer == "yes":  # It needs to be lowercase.
    #    print("That's interesting...")
    # else:
    #    print("Really?")

    answer = messagebox.askyesnocancel(title=" Yes No Cancel", message="Do you like to code?",
                                       icon="warning")
    if answer:  # True
        print("You like to code.")
    elif answer == False:  # False
        print("You don't like to code.")
    else:  # None.
        print("You are very indecisive.")


window = Tk()

button = Button(window, command=click)

button.pack()
window.mainloop()
