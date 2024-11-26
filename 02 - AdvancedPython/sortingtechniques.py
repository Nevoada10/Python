num = [2, 5, 10, 4, 50, 36, 50, 49]
for i in num:
    x = 0

for i in sorted(num, reverse=True):  # Write numbers in descending order.
    print(f"{i}", end=' ')
print()

players = ["Messi", "CR7", "Salah", "Harry"]

for i in sorted(players, reverse=True):
    print(i,end=' ')
print()

for i in sorted(players):
    print(i, end=' ')
print("\n")

d = {'f': 1, 'b': 4, 'a': 3, 'e': 9, 'c': 2}
for x, y in sorted(d.items()):
    print(x, y)
print()

d = {'f': 1, 'b': 4, 'a': 3, 'e': 9, 'c': 2}

for i in sorted(d.items()):
    print(i)
print()

for i in sorted(d.values()):
    print(i)
for i in sorted((d.keys())):
    print(i)
for i in reversed(players):
    print(i)

animals = [{"name": "Dog", "age": 11},
           {"name": "Lion", "age": 30},
           {"name": "Elephant", "age": 63},
           {"name": "Leopard", "age": 18}, ]

for animals in filter(lambda i: i["age"] % 2 == 0, animals):
    print(animals)

country = ["India", "Canada", "Brazil", "Japan", "Israel"]

while country:
    print(country.pop(-1))

print(country)

