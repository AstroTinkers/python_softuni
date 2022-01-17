num_1 = int(input())
num_2 = int(input())

for current_num in range(num_1, num_2 + 1):
    odd_sum = 0
    even_sum = 0
    for index, char in enumerate(str(current_num), start=1):
        if index % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)
    if odd_sum == even_sum:
        print(current_num, end=" ")