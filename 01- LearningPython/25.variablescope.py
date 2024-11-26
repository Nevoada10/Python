# The scope of a variable tells where the variable is recognized.
# 1) Global, global scope.
# 2) Local variable, local scope, inside of a function (unless specified).

name = "Bro"

def display_name():
    name = "Code"
    print(name)

display_name()
print(name)
