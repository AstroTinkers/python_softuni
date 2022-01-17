num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

for i in range(1, num_1 + 1):
    if i % 2 != 0:
        continue
    for j in range(1, num_2 + 1):
        if j not in (2, 3, 5, 7):
            continue
        for k in range(1, num_3 + 1):
            if k % 2 == 0:
                print(f"{i} {j} {k}")