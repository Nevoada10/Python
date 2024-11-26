name = "Bro Code "

#nothing() = self


print(len(name)) # tell you the lenght SPACES ARE INCLUDED.

print(name.find("B")) #find how many of the argument that you want #STARTS AT 0 #If = -1 it means doesn't exist.
print(name.capitalize()) # make the first letter uppercase.
print(name.upper()) # make every single character uppercase.
print(name.lower()) # make every single character lowercase.
print(name.isdigit()) # tells if the variable is only made of numbers, can't have spaces also.
print(name.isalpha()) # tells if the variable is only made of alphabet characters, can't have spaces also.
print(name.count("o")) # tells how much of that appears in the variable, doesn't differentiate uppercase from lowercase.
print(name.replace("o","a")) #replaces every that for other thing in the variable.
print(name*3)