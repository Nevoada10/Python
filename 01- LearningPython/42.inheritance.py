class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal): # Child = Rabbit, Father  = Animal
    def run(self):
        print("This rabbit is running")
    pass
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
    pass
class Bird(Animal):
    def fly(self):
        print("This bird is flying")
    pass

rabbit = Rabbit()
fish = Fish()
bird = Bird()

print(rabbit.alive)
fish.eat()
bird.sleep()

print("-")

rabbit.run()
fish.swim()
bird.fly()