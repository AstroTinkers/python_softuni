n = int(input())
L = int(input())

for i in range(1, n):
    for j in range(1, n):
        for k in range(ord("a"), ord("a") + L):
            for m in range(ord("a"), ord("a") + L):
                for x in range(max(i, j) + 1, n + 1):
                    print(f"{i}{j}{chr(k)}{chr(m)}{x}", end=" ")