# list comprehension = a way to create a new list with less syntax can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]

# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]

# create an empty list
# create a for loop
# define what each loop iteration should do


# FIRST EXAMPLE:

squares = []
for i in range(1, 11):
    squares.append(i * i)

print(squares)

# SECOND EXAMPLE:

squares = [i * i for i in range(1, 11)]

print(squares)

# THIRD EXAMPLE:

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(sorted(filter(lambda x: x >= 60, students)))

print("Passed students:", passed_students)

test = [i for i in range(0, 101, 10)]
passed_students = [i if i >= 60 else "FAILED" for i in test]
print(test)
print(passed_students)
