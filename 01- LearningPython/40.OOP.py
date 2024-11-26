class Car:  # Define class.
    def __init__(self, make, model, year, color):  # Call the constructor.
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Adding modules. # Methods.
    def drive(self):
        print("This " + self.model + " is driving.")

    def stop(self):
        print("This "+self.model+" is stopped")


car1 = Car("Chevy", "Corvette", 2021, "Blue")
car2 = Car("Ford", "Mustang", 2022, "Red")

print('1:\n')

print(car1.make, car1.model)
print(car1.year, car1.color,'\n')

print('2:\n')

car1.drive()
car1.stop()

print('')

car2.drive()
car2.stop()

print("This " + car2.model + " is stopped.")
