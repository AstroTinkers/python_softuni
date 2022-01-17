iterations = int(input())
counter = 0
sum_nechetni = 0
sum_chetni = 0
for i in range(iterations):
    number = int(input())
    counter += 1
    if counter % 2 != 0:
        sum_nechetni += number
    else:
        sum_chetni += number
difference = abs(sum_chetni - sum_nechetni)
if sum_chetni == sum_nechetni:
    print("Yes")
    print(f"Sum = {sum_chetni}")
else:
    print("No")
    print(f"Diff = {difference}")