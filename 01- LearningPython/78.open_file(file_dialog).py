from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(initialdir="/Users/urielnevessilva/Desktop/Programing/Python",
                                          title="Open file okay?",
                                          filetypes=("Text file","*.txt"))  # Creates a
    # string of the path of your file.
    file = open(filepath, 'r')
    print(file.read())
    file.close()
    print(filepath)


window = Tk()
button = Button(text="Open", command=openfile)

button.pack()
window.mainloop()
