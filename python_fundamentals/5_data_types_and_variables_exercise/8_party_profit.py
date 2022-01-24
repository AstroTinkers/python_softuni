group_size = int(input())
adventure_days = int(input())
coins = 0
for i in range(1, adventure_days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    coins += 50 - (group_size * 2)
    if i % 3 == 0:
        coins -= group_size * 3
    if i % 5 == 0:
        coins += 20 * group_size
    if i % 3 == 0 and i % 5 == 0:
        coins -= group_size * 2
profit = int(coins / group_size)
print(f"{group_size} companions received {profit} coins each.")
