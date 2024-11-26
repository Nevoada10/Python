########################################################################################################################
#  Nevoada                                                                                                             #
########################################################################################################################


def main(comma_list):
    unsorted_list = create_list(comma_list)  # O(n) # Creates a list using the user input.
    # check_list(unsorted_list)  # O(n²)
    unsorted_list = remove_duplicates(unsorted_list)  # O(n²) # Remove any repeated number.
    sorted_list = sort_list_by_smallest(unsorted_list)  # O(n²)
    print(f"List sorted: {sorted_list}")  # O(1)
    return 0


def create_list(user_input):
    list_of_strings = user_input.split(",")
    print(f"List of strings: {list_of_strings}", type(list_of_strings))

    integer_list = []

    for strings in list_of_strings:
        integer_list.append(int(strings))

    print(f"List of integers: {integer_list}", type(list_of_strings))

    return integer_list


def remove_duplicates(integer_list):
    unsorted_list = []

    for number in integer_list:
        if number not in unsorted_list:
            unsorted_list.append(number)
    return unsorted_list


def check_list(unsorted_list):
    for index in range(len(unsorted_list)):
        print(f"(I: {index}, N={unsorted_list[index]}", end='); ')

    print("LIST CHECKED SUCCESSFULLY!")
    return 0


def sort_list_by_smallest(unsorted_list):
    sorted_list = []
    while unsorted_list:
        smallest_number = unsorted_list[0]
        smallest_index = 0
        for index in range(len(unsorted_list)):
            if unsorted_list[index] < smallest_number:
                smallest_number = unsorted_list[index]
                smallest_index = index
        sorted_list.append(smallest_number)
        del unsorted_list[smallest_index]
    return sorted_list


main("16,4,17,10,1,2,0,54,62,100")
