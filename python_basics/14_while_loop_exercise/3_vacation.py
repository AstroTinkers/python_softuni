needed_money = float(input())
available_money = float(input())
days = 0
spending_days = 0
while available_money < needed_money:
    action = input()
    action_money = float(input())
    days += 1
    if action == "save":
        available_money += action_money
        spending_days = 0
    else:
        available_money -= action_money
        if available_money < 0:
            available_money = 0
        spending_days += 1
        if spending_days == 5:
            print("You can't save the money.")
            print(days)
            break
else:
    print(f"You saved the money for {days} days.")