owtext = "1) Hello!\nThis is some text!\nYou can use an inversed bar\nAnd add an n after it in the middle of the " \
         "string\nTo break a line\nLike this!\n"
atext = "2) I will append some text to this file, so it won't be overwritten."

with open("/Users/urielnevessilva/Desktop/Programing/Python/a.txt", 'w') as file:  # Overwriting
    # r,to read (by default), or w, to overwrite, a to append.
    # Notice 'w', It will overwrite any previous text in the file.
    file.write(owtext)

# with open("/Users/urielnevessilva/Desktop/Programing/Python/a.txt",'a') as file: # Appending
#   file.write("")
#  file.write(atext)

# If the named file does not exist it will create a new one.
