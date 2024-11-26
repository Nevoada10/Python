tup1 = ("Mercedes", "Audi", "BMW")

iter_tup = iter(tup1)

print(next(iter_tup))
print(next(iter_tup))
print(next(iter_tup))

dict1 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(dict1)
print(dict1["key1"])  # Value associated to key1
print(dict1.get("key4"))
print(dict1.pop("key4"))
print(dict1)
print(sorted(dict1))  # Returns a list of command
print(dict1.keys())
print(dict1.values())
dict1.update({"key4": "value4"})  # Parenthesis and curly bracers.

for x in dict1:
    print(dict1[x])

for x,y in dict1.items():
    print(x,y)

mydict = dict1.copy()
print(mydict

      )
