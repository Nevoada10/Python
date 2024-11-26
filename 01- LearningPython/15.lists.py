# A list is used to store multiple items in a single variable.
# list = [e1,e2,e3]

healthy_food = ["eggs", "chicken", "oatmeal",
"fruits","pizza"]

healthy_food.append("snacks") # adds a new element at the last position of the list.
healthy_food.remove("pizza") # removes a designated element of the list.
healthy_food.pop() #removes the last element of the list.
healthy_food.insert(0,"salad")

print(healthy_food)

healthy_food.sort()

print(healthy_food)

for x in healthy_food:
    print(x)

healthy_food.clear()

print(".",healthy_food)