import random
import time
import math

# INITIAL DEF:

BPM = 120  # float(input("BPM = "))
counter1 = 0


# FUNCTIONS DEF:
# Define the 'counter1' function
def increment_counter1():
    global counter1  # Use the 'global' keyword to access the 'counter1' variable outside the function's scope
    counter1 += 1


def read_list(list_1xn):
    for fingers in list_1xn:
        time.sleep(60 / BPM)
        print(fingers)
        increment_counter1()
    print("-")


def repeat_function(n, function, *args, **kwargs):
    for i in range(n):
        function(*args, **kwargs)


# CODE:

# Choose a pattern

while True:
    try:
        order_list = []
        model_list = [1, 2, 3, 4]

        while model_list:
            random_element = random.choice(model_list)
            order_list.append(random_element)
            model_list.remove(random_element)

        # Display Pattern

        print("Pattern", order_list)
        print("-")
        time.sleep(2)

        # Repeat the read_list function 4 times

        repeat_function(4, read_list, order_list)

        # Exception handling, counter1 printing.

    except KeyboardInterrupt as e:
        print(e)
        print(counter1)
        counter2 = math.floor(counter1/4)
        print(counter2)
        break
