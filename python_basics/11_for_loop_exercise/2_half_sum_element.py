import sys
iterations = int(input())
num_max = -sys.maxsize
sum_numbers = 0
for i in range(iterations):
    number = int(input())
    sum_numbers += number
    if number > num_max:
        num_max = number
sum_numbers -= num_max
difference = abs(num_max - sum_numbers)
if num_max == sum_numbers:
    print("Yes")
    print(f"Sum = {num_max}")
else:
    print("No")
    print(f"Diff = {difference}")