# STRINGS
# Def
first_name = "Bro"
last_name = "Code"
full_name = first_name + last_name

# Type()
print("First name type:", type(first_name))
print("Last name type:", type(last_name))
print("Full name type:", type(full_name))

# Display
print("Hello " + full_name)
print("Hello", full_name)

# You can't mix variable types.
# don't do this
# age = "21"
# age +=1
#  File "/Users/urielnevessilva/PycharmProjects/helloWorld/part2variables.py", line 19, in <module>
# age +=1
# ^^^^^^^
# TypeError: can only concatenate str (not "int") to str

# Comentário longo """ comentário """, mas parece não funcionar no Pycharm.

# INTEGERS

age = 21
age += 1  # or age = age + 1

print("Your age is:", age)  # first way
print("Your age is: " + str(age))  # convert way

# FLOAT

height = 250.5
print("I have " + str(height) + " centimeters.")
print(type(height))

# BOOLEANO, BOOLEAN

human = True
print("Are you a human? " + str(human))
print(type(human))
