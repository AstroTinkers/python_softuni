destination = input()
budget_min = float(input())
end_of_vacation = False
money_collected = 0

while not end_of_vacation:
    money = float(input())
    money_collected += money
    if money_collected >= budget_min:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End":
            end_of_vacation = True
            break
        budget_min = float(input())
        money_collected = 0
