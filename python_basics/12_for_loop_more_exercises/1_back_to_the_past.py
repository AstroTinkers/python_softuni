moneyt_inherited = float(input())
year_to_live = int(input())
money_to_live = 0
for i in range(1800, year_to_live + 1, 1):
    if i % 2 == 0:
        money_to_live += 12000
    else:
        money_to_live += 12000 + 50*((18 + i) - 1800)
difference = abs(money_to_live - moneyt_inherited)
if moneyt_inherited >= money_to_live:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")