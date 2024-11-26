# If, elif, else

age = int(input("How many years old are you? "))

if age > 100:
    print("You are alive for more than one century!")
elif age == 100:
    print("You are a century old.")
elif age >= 18:
    print("You are a legal adult.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are a minor.")
