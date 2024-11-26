# sort method = used with lists
# sort () function = used with other iterables

def iteration_print(iterable):
    for i in iterable:
        print(i)


def filter_used(number, ordination_type):
    print("-")
    print(number, ") Sorted by", ordination_type, ":")


students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Crabs"]

students.sort(reverse=True)  # Reverse alphabetical order.   # Sorting.
sorted_students = sorted(students)   # Sorting.
filter_used(1, "Reverse alphabetical order")
iteration_print(students)

print("-")
print("2 ) Sorted function, used with tuples for example.")
iteration_print(sorted_students)


students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr . Krabs", "C", 78)]
# 3
students.sort()  # Sorting.
filter_used(3, "First element(name)")
iteration_print(students)

# 4
grade = lambda grades: grades[1]
students.sort(key=grade)  # Sorting.
filter_used(4, "Grades")
iteration_print(students)

# 5
grade = lambda grades: grades[1]
students.sort(key=grade, reverse=True)  # Sorting.
filter_used(5, "Age and Reversed")
iteration_print(students)

# 6
ages = lambda age: age[2]
students.sort(key=ages)  # Sorting.
filter_used(6, "Age")
iteration_print(students)

# 7, w/ tuples.

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr . Krabs", "C", 78))

age = lambda ages: ages [2]
sorted_students = sorted(students, key=age)     # Sorting
filter_used(7,"Tuples")
iteration_print(students)
