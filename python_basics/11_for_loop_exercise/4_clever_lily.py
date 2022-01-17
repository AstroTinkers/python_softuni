lily_age = int(input())
price_washing_machine = float(input())
price_toy = int(input())
money_birthday = 0
brother_money = 0
counter = 0
toys = 0
for i in range(lily_age):
    counter += 1
    if counter % 2 == 0:
        money_birthday += (counter / 2) * 10
        brother_money += 1
    else:
        toys += 1
money_toys = price_toy * toys
money_birthday_final = money_birthday - brother_money
difference = abs((money_toys + money_birthday_final) - price_washing_machine)
if money_toys + money_birthday_final >= price_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")