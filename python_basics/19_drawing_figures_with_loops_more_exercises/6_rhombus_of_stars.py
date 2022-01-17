n = int(input())

for i in range(1, n + 1):
    print((n-i) * " ", end="")
    print("*", end="")
    print((i - 1) * " *", end="")
    print()
for j in range(n - 1, 0, -1):
    print((n-j) * " ", end="")
    print("*", end="")
    print((j - 1) * " *", end="")
    print()