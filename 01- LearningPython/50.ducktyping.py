# Duck Typing = Concept where the class is not as important as it's methods/attributes.
# Class type isn't checked if minimum methods or attributes are present.
# " If it walks like a duck, and it quacks like a duck, them it's a duck. "

class Duck:
    @staticmethod
    def walk():
        print(" This duck is walking.")

    @staticmethod
    def talk():
        print(" This duck is quacking. ")

    # Duck Typing = Concept where the class is not as important as it's methods/attributes.
    # Class type isn't checked if minimum methods or attributes are present.
    # " If it walks like a duck, and it quacks like a duck, them it's a duck. "

    class Duck:
        @staticmethod
        def walk():
            print(" This duck is walking.")

        @staticmethod
        def talk():
            print(" This duck is quacking. ")

        def __str__(self):
            return "duck"

    class Chicken:
        @staticmethod
        def walk():
            print(" This chicken is walking.")

        @staticmethod
        def talk():
            print(" This chicken is clucking. ")

        def __str__(self):
            return "chicken"

    class Person:
        @staticmethod
        def catch(animal):
            animal.walk()
            animal.talk()
            print(" You caught the {}.".format(animal))

    duck = Duck()
    chicken = Chicken()
    person = Person()

    person.catch(duck)
    print(" -")
    person.catch(chicken)

    def __str__(self):
        return "duck"


class Chicken:
    @staticmethod
    def walk():
        print(" This chicken is walking.")

    @staticmethod
    def talk():
        print(" This chicken is clucking. ")

    def __str__(self):
        return "chicken"


class Person:
    @staticmethod
    def catch(animal):
        animal.walk()
        animal.talk()
        print(" You caught the {}.".format(animal))


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
print(" -")
person.catch(chicken)
