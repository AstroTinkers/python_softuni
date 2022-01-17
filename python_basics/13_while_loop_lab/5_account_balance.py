money = input()
sum_money = 0
while money != "NoMoreMoney":
    if float(money) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(money):.2f}")
    sum_money += float(money)
    money = input()
print(f"Total: {sum_money:.2f}")