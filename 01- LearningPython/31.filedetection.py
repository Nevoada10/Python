import os

directory = "/Users/urielnevessilva/Desktop/Programing/Python/a.txt"

if os.path.exists(directory):  # Mostra se o caminho existe!
    print("The path exists", end="")
    if os.path.isfile(directory):
        print(", it's a file.")
    elif os.path.isdir(directory):
        print(", this is a directory.")
    else:
        print(", but I don't know what it's it.")
else:
    print("The path doesn't exists.")
