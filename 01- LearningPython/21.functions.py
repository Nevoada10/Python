def greeting(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name,end=". ")
    print("you are "+age+" "+"years old.")

value1 = input("First Name: ")
value2 = input("Last Name: ")
value3 = input("Age: ")

greeting(value1,value2,value3)
greeting("Bo","Terfly","21")