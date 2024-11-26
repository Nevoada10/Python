# filter () = creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

def print_list(generic_list):
    for pairs in generic_list:
        print(pairs)


friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

# age = lambda data: data[1] >= 18
# adult_friends = list(filter(age, friends))

adult_friends = list(filter(lambda x: x[1] >= 18, friends))  # LIST
adult_friends_sorted_by_age = list(sorted(adult_friends, key=lambda age: age[1], reverse=True))
# Iterable , key , # reverse.
print_list(adult_friends)
print("-")
print(adult_friends_sorted_by_age)
