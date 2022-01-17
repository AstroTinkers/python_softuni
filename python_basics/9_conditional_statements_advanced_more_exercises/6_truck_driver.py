season = input()
km_month = float(input())

if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        pay = 0.75
    elif season == "Summer":
        pay = 0.9
    elif season == "Winter":
        pay = 1.05
elif 5000 < km_month and km_month <=10000:
    if season == "Spring" or season == "Autumn":
        pay = 0.95
    elif season == "Summer":
        pay = 1.1
    elif season == "Winter":
        pay = 1.25
elif 10000 < km_month and km_month <= 20000:
    pay = 1.45

salary = (pay * km_month) * 4
salary_final = salary * 0.9
print(f"{salary_final:.2f}")