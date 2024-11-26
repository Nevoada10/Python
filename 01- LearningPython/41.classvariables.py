class Car:  # Define class.

    number_wheels = 4  # Class variable, because it applies to every single vehicle in that category.

    def __init__(self, make, model, year, color):  # Call the constructor.
        self.make = make  # Instance variable.
        self.model = model  # Instance variable.
        self.year = year  # Instance variable.
        self.color = color  # Instance variable.

# Instance variables are mostly unique for each object, and you need to specify them while constructing the object.

    # Adding modules.
    def drive(self):
        print("This " + self.model + " is driving.")

    def stop(self):
        print("This " + self.model + " is stopped.")


car1 = Car("Chevy", "Corvette", 2021, "Blue")
car2 = Car("Ford", "Mustang", 2022, "Red")
car3 = Car("Dodge", "Charger", 2018, "Green")
car4 = Car("Flying", "Car", 2073, "Silver")

car4.number_wheels = 0

print("Car 1 has:", car1.number_wheels, "wheels.")
print("Car 2 has:", car2.number_wheels, "wheels.")
print("Car 3 has:", car3.number_wheels, "wheels.")
print("Car 4 has:", car4.number_wheels, "wheels.")
