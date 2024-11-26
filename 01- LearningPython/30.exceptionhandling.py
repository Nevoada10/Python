# exception = events detected during the execution, that interrupt the flow of a program.
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to be divided: "))
    result = numerator / denominator  # float conversion.
    print(type(result))

# Catch specific expections first:
except ZeroDivisionError as e:
    print("You can't divide by zero.")
    print(e)
except ValueError as e:
    print("Enter only numbers.")
    print(e)
except Exception as e:
    # print("Something went wrong.")
    print(e)

else:  # If there is no exceptions.
    print("Result:", result)

finally:  # Will execute anyways at the end.
    print("Process finished.")

# This code is dangerous, because of the division by zero.
