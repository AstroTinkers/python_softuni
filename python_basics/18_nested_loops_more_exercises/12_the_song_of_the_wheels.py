control_number = int(input())
counter = 0
num_found = False
combination = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a >= b:
                    break
                if c <= d:
                    break
                if a * b + c* d == control_number:
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        combination = (a, b, c, d)
                        num_found = True
if num_found:
    print(f"\nPassword: {combination[0]}{combination[1]}{combination[2]}{combination[3]}")
else:
    print(f"\nNo!")
