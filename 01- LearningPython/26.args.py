# *args (or any other name) is a command packs all arguments into a tuple.
# useful for functions that vary their amount of parameters (and the order is not important)
def function(*numbers):#tuple
    sum = 0
    numbers = list(numbers) # numbers is a list
    numbers[5] = 5
    for elements in numbers:
        sum += elements
    print(sum)
    return sum

function(1,2,3,4,5,6)