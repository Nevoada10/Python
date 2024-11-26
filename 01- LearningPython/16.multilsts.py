# 2D lists = list of lists (Matrix)

drinks = ["coffe","soda","tea"]
dinner = ["pizza"," hamburger","hotdog"]
dessert =["cake","ice cream"]

food = [drinks,dinner,dessert]

print(food[0][1])

for i in food:
    print(i)
print('')
print(food)
print('')


drinks = ["coffe", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

for lst in food:
    print(",".join(lst)) # juntar os elementos de cada iteração em uma única string.
