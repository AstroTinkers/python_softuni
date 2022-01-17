iterations = int(input())
left_sum = 0
for i in range(iterations):
    current_sum = int(input())
    left_sum = current_sum + left_sum
right_sum = 0
for i in range(iterations):
    current_sum = int(input())
    right_sum = current_sum + right_sum
difference = abs(left_sum - right_sum)
if right_sum == left_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")