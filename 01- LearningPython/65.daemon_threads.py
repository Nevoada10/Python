# **********************************************************
# Python daemon threads
# **********************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long-running processes

import threading
import time


def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for", count, "seconds.")


x = threading.Thread(target=timer, args=(), daemon=True)
# x.setDaemon(True) # setDaemon() is deprecated, set the daemon attribute instead # Sets a thread to Daemon
# if it's not currently running

# print(x.isDaemon()) # x.isDaemon() is deprecated, set the daemon attribute instead #

# What is a deprecation warning?
# They are warnings that notify us that a specific feature (e.g. a method) will be removed soon (usually in the n
# ext minor or major opens a new window version) and should be replaced with something else.

x.start()

answer = input("Type anything when you want to stop? \n")
