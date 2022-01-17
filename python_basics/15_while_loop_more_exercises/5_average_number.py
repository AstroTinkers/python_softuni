n = int(input())
sum_num = 0
for i in range(n):
    number = int(input())
    sum_num += number
average = sum_num / n
print(f"{average:.2f}")