# The "inner loop" will finish all of its iterations before
# Finishing one iteration of the "outer loop.

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")
iterations = 0

# i stats at 0
# j starts at 0

for i in range(0, 2 + 1):  # 0 - 2
    for j in range(0, 2 + 1):  # 0 - 2
        print("j=", j)
    print("i=", i)

    # vai de 0 a 2 duas vezes.

for i in range(0, rows):  # rows iterações
    for j in range(0, columns):  # columns iterações
        print(symbol, end=" ")  # Ao invés de printar uma coluna, o end = " " vai
        # substitutir o fim de cada iteração por um espaço em branco, permitindo
        # que eles fiquem lado a lado.
        iterations += 1
    print()  # printar uma nova linha toda vez que j terminar.

print("Iterations = " + str(iterations))
