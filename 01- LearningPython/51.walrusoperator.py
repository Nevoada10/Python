# Walrus Operator: :=

# Assignment expression.
# Assign values to variables as part of a larger expression.
# Simplify or reduce the amount of lines of code.

# Code 1:
"""

print(a := True)  # Defines and prints "a" at the same time.
print(a)

print(" -")

"""
# Code 2:

foods = list()  # foods = []

while True:
    food = input("What food do you like? ")
    if food == "quit":
        break
    foods.append(food)

print(foods)

"""
#Code 3

list_foods = list()  # foods = []

while food := input("What food do you like? ") != "quit":  # New to Python 3.8
    list_foods.append(food)

print(list_foods)

"""
