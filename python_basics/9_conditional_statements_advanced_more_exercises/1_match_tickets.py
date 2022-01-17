budget = float(input())
category = input()
people = int(input())

if 1<= people and people <= 4:
    transport = budget * 0.75
elif 5<= people and people <= 9:
    transport = budget * 0.6
elif 10<= people and people <= 24:
    transport = budget * 0.5
elif 25<= people and people <= 49:
    transport = budget * 0.4
elif people >= 50:
    transport = budget * 0.25

if category == "VIP":
    ticket = 499.99
elif category == "Normal":
    ticket = 249.99

expences = transport + ticket * people
difference = abs(budget - expences)

if budget >= expences:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < expences:
    print(f"Not enough money! You need {difference:.2f} leva.")