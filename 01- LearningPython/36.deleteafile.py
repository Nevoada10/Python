import os
import shutil
import time

# os.remove(path) # Removes a file from the designated path.
# os.rmdir(path) # Removes an empty folder.
# shutil.rmtree(path) #

src = "/Users/urielnevessilva/Desktop/Programing/Python/36deleteafiletest/c.txt"
answer = 0
txt = "Hello"


def timer(seconds):
    for i in range(seconds, 0, -1):  # 10 - 1
        print(i)  # print
        time.sleep(1)  # time interval between iterations.


def remove_file(source):
    os.remove(source)
    print("Removing file...")
    timer(3)
    print(os.path.basename(source), "was deleted from", source)


def create_file(source, text):
    with open(source, 'w') as file:
        file.write(text)
        print("Creating file...")
        timer(3)
        print("The file", os.path.basename(source), "was created in", source, ".")


try:
    remove_file(src)
except FileNotFoundError:
    while answer != ("Y" and "N"):
        answer = input("This file was not found! Do you want to create a new file? (Y/N): ").upper()
        if answer == "Y":
            create_file(src, txt)
            break
        elif answer == "N":
            break
except PermissionError:
    print("You don't have permission to do that")
    """try:
        print("You don't have permission to do that, deleting folder...")
        os.rmdir(src)
        timer(3)
    except OSError:
        while answer != ("Y" and "N"):
            answer = input("This is not an empty folder, do you want to delete it? (Y/N): ").upper()
            if answer == "Y":
                shutil.rmtree(src)
                break
            elif answer == "N":
                break"""
except OSError:
    print("OS Error, It's not an empty folder!")
except Exception as e:
    print("Exception:", end=" ")
    print(e)

print("This program has finished.")
