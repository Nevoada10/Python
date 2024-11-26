# Thread = a flow of execution. Like a separate order of instructions.
#                  However, each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu-bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            uses multithreading

# eat_breakfast():
# drink_water():
# study():

import threading
import time


# Define functions for different tasks


def eat_breakfast():
    time.sleep(3)
    print("You drank coffee")


def drink_water():
    time.sleep(4)
    print("You drank water")


def study():
    time.sleep(5)
    print("You have studied")


# Define a function to measure elapsed time

def timer():
    start_time = time.time()  # Record the start time
    x.join()  # Wait for thread x to finish
    y.join()  # Wait for thread y to finish
    z.join()  # Wait for thread z to finish
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    formatted_elapsed_time = "{:.3f}".format(elapsed_time)  # Format elapsed time with 3 decimal places
    print("Elapsed time: {} seconds".format(formatted_elapsed_time))  # Print formatted elapsed time


# Create threads to execute the functions

x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_water, args=())
z = threading.Thread(target=study, args=())

# Create a timer thread

t = threading.Thread(target=timer, args=())

# Start the threads for tasks

x.start()
y.start()
z.start()

# Start the timer thread

t.start()

# Checking how many threads are active:

c = threading.active_count()
print(c)
print(threading.enumerate())

# Wait for all threads to finish for tasks

x.join()
y.join()
z.join()

# Wait for the timer thread to finish

t.join()

# Additional last print statements

print("Wo/ multithreading time:", 3 + 4 + 5, "seconds")
print("All {} threads have finished.".format(c))
print("Time elapsed for the main thread:", time.perf_counter())

# Main thread plus extra threads
