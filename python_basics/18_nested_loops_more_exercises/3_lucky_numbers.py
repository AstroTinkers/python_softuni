number = int(input())
if number < 10:
    check = number
else:
    check = 10
for i in range(1, check):
    for j in range(1, check):
        if number % (i + j) != 0:
            continue
        for k in range(1, check):
            for m in range(1, check):
                if i + j == k + m:
                    print(f"{i}{j}{k}{m}", end=" ")
