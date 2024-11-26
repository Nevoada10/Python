from tkinter import *


def submit():
    print("The temperature is " + str(scale.get()) + " degrees Celsius.")


window = Tk()
window.geometry("200x900")

directory = "/Users/urielnevessilva/Desktop/background.png"

Top_Image = PhotoImage(file=directory)
Bottom_Image = PhotoImage(file=directory)

Top_Label = Label(window,
                  image=Top_Image)

Bottom_Label = Label(window,
                     image=Bottom_Image)

scale = Scale(window,
              from_=100, to=0,  # FROM = from
              length=600,
              orient=VERTICAL,  # Orientation of scale # HORIZONTAL # VERTICAL
              font=("Consolas", 20),
              showvalue=True,  # TRUE # FALSE # 0 or 1 # Displays the value on the display or not.
              tickinterval=10,
              resolution=1,  # Increment of slider.# 5 means he "walks" 5 points in the scale each walk.
              troughcolor="Light blue",  # Color of the "tube" where the slider will go through.
              fg="White",
              bg="Grey"

              )
button = Button(window,
                text="Submit",
                font=("Consolas", 20),
                fg="Grey",
                bg="White",
                command=submit,
                )

# scale.set(50)  # Sets where the slider starts at the program. # Fixed amount
scale.set(
    (scale["from"] - scale["to"] / 2) + scale["to"])  # Slider start relative to percentage # From without underscore _.

Top_Label.pack()
scale.pack()
Bottom_Label.pack()
button.pack(anchor=S)  # OR side=___
window.mainloop()
