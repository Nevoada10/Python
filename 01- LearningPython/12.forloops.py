# "For" loops will execute your code for a limited amount of times.
# While = unlimited.
# For = limited
# for i in range (start inclusive, stop exclusive, steps):


# for index in range(50,100+1): #will iterate n+1 times, so 101-50 = 51 iterations.
# print(index)

# for i in range (10): # 0 - 9
# print (i+1) # 1 - 10

# for i in range(50,100+1): #will iterate n+1 times, so 101-50 = 51 iterations.
# print(i) # 50 - 100

# for i in range (50,100+1,2):
# print(i)

# You can iterate through anything that is considered iterable, like strings.

# for i in "Bro Code":
# print(i)

"""  
B
r
o

C
o
d
e
"""
import time

for i in range(10, 0, -1):  # 10 - 1
    print(i)  # prints
    time.sleep(1)  # time interval between iterations.
print("Happy New Year!")
