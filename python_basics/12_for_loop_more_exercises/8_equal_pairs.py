import sys
n_pairs = int(input())
max_difference = 0
previous_num = 0
for i in range(n_pairs):
    num1 = int(input())
    num2 = int(input())
    if i > 0:
        if abs(previous_num - num1 - num2) > max_difference:
            max_difference = abs(previous_num - num1 - num2)
    previous_num = num1 + num2
if max_difference == 0:
    print(f"Yes, value={previous_num}")
else:
    print(f"No, maxdiff={max_difference}" )