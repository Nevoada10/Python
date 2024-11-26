try:
    with open(
            "/Users/urielnevessilva/Desktop/Programing/Python/a.txt") as file:  # path or string file name (if it's
        # in the Pycharm projects folder)
        # /Users/urielnevessilva/Desktop/Programing/Python/a.txt
        print(file.read())
except FileNotFoundError:
    print("This file was not found.")
except exception as e:
    print(e)

print(file.closed)  # Shows if the file is closed.
