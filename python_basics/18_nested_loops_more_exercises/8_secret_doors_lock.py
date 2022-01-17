hundreds_max = int(input())
tens_max = int(input())
singles_max = int(input())

for i in range(1, hundreds_max + 1):
    if i % 2 == 0:
        for j in range(1, tens_max + 1):
            if j in [2, 3, 5, 7]:
                for k in range(1, singles_max + 1):
                    if k % 2 == 0:
                        print(f"{i} {j} {k}")