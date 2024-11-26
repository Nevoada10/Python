# Multiple Inheritance =  When a child class is derived from more than one parent class.

class Prey:
    def flee(self):
        print("This animal flees.")


class Predator:
    def hunt(self):
        print("This animal hunts.")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()  # Prey
hawk = Hawk()  # Predator
fish = Fish()  # Prey & Predator
