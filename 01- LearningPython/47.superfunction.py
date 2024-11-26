"""
Super Function = Function used to give access to the methods of the parent class.
Returns a temporary object of a parent class when used.
"""


# Code 1:


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


class RectangularPrism(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height

    def volume(self):
        return Rectangle.area(self) * self.height


rectangle = Rectangle(3, 4)
rectangular_prism = RectangularPrism(3, 4, 5)

print("Rectangle Area : " + str(rectangle.area()) + " m²")

print("-")

print("Rectangular Prism Side Area 2: " + str(rectangular_prism.area()) + " m²")
print("Rectangular Prism Volume 2: " + str(rectangular_prism.volume()) + " m³")


########################################################################################################
# Code 2:
class Animal:
    def make_noise(self):
        print("Some generic animal noise.")


class Dog(Animal):
    def make_noise(self):
        super().make_noise()
        print("Woof woof!")
