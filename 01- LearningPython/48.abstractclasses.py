# Prevents user from creating an object of that class.
# Compels the user to override abstract methods in a child class.

# Abstract class = a class which contains abstract methods.
# Abstract method = a method that has a declaration but no implementation.

from abc import ABC, abstractmethod


class Vehicle(ABC):  # Template.

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Code:

class Car(Vehicle):

    def go(self):  # Method overwriting.
        print("You drive the car.")

    def stop(self):
        print("This car is stopped.")


class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motorcycle.")  # Method overwriting.

    def stop(self):
        print("This motorcycle is stopped.")


car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

"""
vehicle = Vehicle()
vehicle.go()

Traceback (most recent call last):
  File "/Users/urielnevessilva/PycharmProjects/helloWorld/48.abstractclasses.py", line 31, in <module>
    vehicle = Vehicle()
              ^^^^^^^^^
TypeError: Can't instantiate abstract class Vehicle with abstract method go
"""