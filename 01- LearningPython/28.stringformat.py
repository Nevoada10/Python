# str.format() = optional method that gives users
# more control when displaying output.

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}.".format(animal,item)) # order
#print("The {0} jumped over the {1}.".format(animal,item)) # any order

## No need for variables declared.
#print("The {animal} jumped over the {animal}.".format(animal="cow",item="moon"))
##

name = "Bro"

text = "The {} jumped over the {}."
print(text.format(animal,item))
print("Hello,my name is {:10}. Nice to meet you!".format(name)) # will use 10 spaces for the variable.
print("Hello,my name is {:<10}. Nice to meet you!".format(name)) # to the left # won't make diff because it's the default..
print("Hello,my name is {:>10}. Nice to meet you!".format(name)) # to the right.

print("Hello my name is {0:^10}. NIce to meet you!".format(name)) # center, using pos arg.
print("Hello my name is {yourname:^10}. NIce to meet you!".format(yourname="Code")) # center, using kw arg.


# Format() using numbers.

number = 10/7
print("The result is {:.3f}.".format(number)) # 3 decimals.

number = 1000.1
print("The result is {:.0f}".format(number)) # int.

number = 17
print("{0} is {0:b} in binary.".format(number)) # binary.
print("{0} is {0:o} in octa.".format(number)) # octa.
print("{0} is {0:X} in hexa.".format(number)) # X for uppercase, x for lowercase.
print("{0} is {0:e} in scientific notation.".format(number))  #E for uppercase, e for lowercase.