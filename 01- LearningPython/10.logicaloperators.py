# and,or,not

temperature = float(input("What is the temperature today? (In Celsius degrees) "))

if not (0 <= temperature <= 30):
    print("The temperature is good today!")
    print("Go outside!")
elif not (temperature < 0 or 30 < temperature):
    print("The temperature not good today!")
    print("Stay inside!")
