# lambda function = function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression.
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)
# lambda parameters: expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + 2
full_name = lambda first_name, last_name: first_name+" "+ last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(18))

"""
double = lambda x:× * 2 multiply = lambda x, y: × * y
add = lambda x, y, z: x + y + 2
full name = lambda first_name, last_name: first_name+" "+ last_name
age check = lambda age:True if age >= 18 else False
print(age_check(18))
"""