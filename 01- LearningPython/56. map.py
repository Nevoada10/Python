# applies a function to each item in an iterable (list, tuple, etc.)
# map (function, iterable)

store_dollars = [("shirt", 20.00),
                 ("pants", 25.00),
                 ("jacket", 50.00),
                 ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1] / 0.82)

store_euros = list(map(to_euros, store_dollars))
store_dollars = list(map(to_dollars, store_euros))

print("\n1) Euros: \n")
for pair in store_euros:
    print(pair)

print("\n2) Dollars: \n")
for pair in store_dollars:
    print(pair)
