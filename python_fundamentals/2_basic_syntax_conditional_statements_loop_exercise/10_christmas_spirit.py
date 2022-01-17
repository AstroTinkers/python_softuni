quantity = int(input())
days = int(input())
cost = 0
happiness = 0
final_day = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        cost += 2 * quantity
        happiness += 5
    if i % 3 == 0:
        cost += 5 * quantity + 3 * quantity
        happiness += 13
    if i % 5 == 0:
        cost += 15 * quantity
        happiness += 17
    if i % 3 == 0 and i % 5 == 0:
        happiness += 30
    if i % 10 == 0:
        happiness -= 20
        cost += 5 + 3 + 15
    final_day += 1
if final_day % 10 == 0:
    happiness -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {happiness}")