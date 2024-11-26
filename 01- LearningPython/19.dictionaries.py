# Dictionaires: A changeable unordered collection of unique key,value pairs.
# Fast because they allow hashing, acess the value quickly.

capitals = {"USA":"Washington DC", # key, value
            "Brazil":"Brasília",
            "France":"Paris",
            "Italy":"Roma"}

capitals.update({"Germany":"Berlim"}) # adds a pair to the dictionary.
capitals["USA"]= "Gotham City" # change a key
capitals.pop("Brazil") # removes a pair.

print(capitals)

print("-")

for key in capitals.keys(): # will print keys only
    print(key)

print("-")

for value in capitals.values():
    print(value)

print("-")

for key,value in capitals.items():
    print(key,",",value)

capitals.clear() # clears the whole dictionary elements.

print(capitals)

#print(capitals.items())
#print(capitals["Brazil"]) # not safe because it might stop your code! use .get instead.
#print(capitals.get("USA")) # better to use!
#print(capitals.keys()) # at the left
#print(capitals.values()) # at the right
# capitals.pop("Brazil") # removes a pair from the dictionary.