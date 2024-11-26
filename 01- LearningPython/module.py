def timer(seconds):
    import time
    for i in range(seconds, 0, -1):  # 10 - 1
        print(i)  # print
        time.sleep(1)  # time interval between iterations.


def create_file(source, text):
    import os
    with open(source, 'w') as file:
        file.write(text)
        print("Creating file...")
        timer(3)
        print("The file", os.path.basename(source), "was created in", source, ".")


def move_file(source, destination):
    import os
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


def remove_file(source):
    import os
    os.remove(source)
    print("Removing file...")
    timer(3)
    print(os.path.basename(source), "was deleted from", source)
