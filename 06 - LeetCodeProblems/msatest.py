import random

def generate_random_list():
    """
    Generates a random list of integers between 0 and 100.
    The length of the list is a random number between 1 and 10.
    
    Returns:
        list: A list of random integers.
    """
    list_length = random.randint(1, 10)
    return [random.randint(0, 100) for _ in range(list_length)]

def extract_non_descending_sublist(random_list):
    """
    Extracts the longest non-descending sublist from the start of the given list.
    
    Args:
        random_list (list): The list from which to extract the sublist.
    
    Returns:
        list: The longest non-descending sublist.
    """
    if not random_list:
        return []

    sublist = [random_list[0]]
    for i in range(1, len(random_list)):
        if random_list[i-1] <= random_list[i]:
            sublist.append(random_list[i])
        else:
            break
    return sublist

# Generate a two random lists
random_list = generate_random_list()
random_list2 = generate_random_list()
print("Original list:", random_list)

# Extract the non-descending sublist
non_descending_list = extract_non_descending_sublist(random_list)
print(non_descending_list)

# Count the number of elements in the non-descending sublist
counter = len(non_descending_list)
print("Counter:", counter)
