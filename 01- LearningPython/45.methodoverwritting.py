"""
Method overwriting: It's a way to a child modify the methods inherited by the parent class.
This is called "METHOD SIGNATURE".
1) Rewrite the method in the child class, using the same structure (parameters...)
"""


class Animal:
    def eat(self):
        print("This animal is eating.")


class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot.")


rabbit = Rabbit()
rabbit.eat()
