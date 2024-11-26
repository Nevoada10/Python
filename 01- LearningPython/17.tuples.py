# Tuple =  collection which is ordered and unchangeable.
# used to group together related data.

student = ("Bro",21,"male")

print("There is/are "+str(student.count("Bro"))+" Bro/Bros")
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")

