# set = collection which is unordered, unindexed, no duplicate values.
# Good to verify if there is a "x" element, faster than lists.

utensils = {"fork","spoon","knife","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin") # adds an element to a set.
#utensils.remove("fork") # removes an element of a set.
#utensils.update(dishes) # updates one set by adding elements from another.
print("Intersection:",utensils.intersection(dishes)) # shows elements that appear in both sets.
print("Difference:",utensils.difference((dishes))) # shows what's in A that is not in B.

dinner_table = utensils.union(dishes) # creates a NEW set using elements of the ones that
# already exist.

for x in dinner_table:
    print("DTi",x)

print(dinner_table)
utensils.clear()
print(utensils)