number = int(input())
for i in range(1, number + 1):
    sum_of_digits = sum(int(digit) for digit in str(i))
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
