int_string = input()
count_beggars = int(input())
queue_line = int_string.split(", ")
home_money = [0] * count_beggars
while len(queue_line) > 0:
    for i in range(count_beggars):
        home_money[i] += int(queue_line[0])
        queue_line.pop(0)
        if len(queue_line) == 0:
            break
print(home_money)
