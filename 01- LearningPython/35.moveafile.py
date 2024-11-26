# or C:\\Users\\urielnevessilva\\Desktop\\Programing\\Python\\a.txt #In Windows for example.
# / = \\, never use \ only when writing a directory, because it can be interpreted as an escape character.
# An "escape" is a special character that has a meaning inside a string, like {} or /n.

import os


# 1) Create a file function:
def create_file(source, text):
    with open(source, 'w') as file:  # Overwriting
        file.write(text)
        print("File", os.path.basename(source), "created.")


# 2) Move the file function.

def move_file(source, destination):
    try:
        if os.path.exists(destination):
            print("The destination path exists,", end=" ")
            if os.path.isfile(destination):  # Checking if there is a file there.
                print("but there is already a file there.")
                answer = ""

                while answer != ("Y" and "N"):
                    answer = input("Do you want to overwrite it? (Y/N): ").upper()  # Asking the user to overwrite the
                    # file.
                    if answer == "Y":
                        print("The {1} document content replaced {0} content.".format(os.path.basename(destination),
                                                                                      os.path.basename(source)))
                        os.replace(source, destination)  # Move the file
                        break
                    elif answer == "N":
                        print("Okay, I won't overwrite {} !".format(os.path.basename(destination)))
                        break
            else:
                os.replace(source, destination)
                print("The {} document was moved.".format(os.path.basename(source)))

    # EXCEPTIONS:
    except FileNotFoundError:
        print("{} was not found.".format(os.path.basename(source)))
    except Exception as e:
        print("An error occurred: ", str(e))


# Initial Stage, Printing.
print("This program will move a file from a source to it's destination.")
print("If there is not file in the source, the program will create one.")
print("If there is a file in the destination you will have the option to overwrite it.")

# Variables needed:
owtext = "1) Hello!\nThis is some text for Botterfly!\nHave a nice day!"  # String, text file content.
src = "/Users/urielnevessilva/Desktop/Programing/Python/a.txt"  # String, source path.
# If no file, the program will create one.
dest = "/Users/urielnevessilva/Desktop/Programing/Python/35moveafiletest/c.txt"  # String, destination path.

# Execution:
create_file(src, owtext)
move_file(src, dest)

# Final Step, Printing:
print("Source Path:", src)
print("Destination Path:", dest)
print("This program has finished.")
