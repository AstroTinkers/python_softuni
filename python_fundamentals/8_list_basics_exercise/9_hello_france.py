items = [i.split("->") for i in input().split("|")]
items = [(i[0], float(i[1])) for i in items]
budget = float(input())
working_budget = budget
sales = []
for (item, price) in items:
    if item == "Clothes" and price > 50.00:
        continue
    elif item == "Shoes" and price > 35.00:
        continue
    elif item == "Accessories" and price > 20.50:
        continue
    else:
        if working_budget >= price:
            working_budget -= price
            sales.append(price * 1.4)
        else:
            break
profit = abs(budget - working_budget - sum(sales))
for c in range(len(sales)):
    print(f"{sales[c]:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")