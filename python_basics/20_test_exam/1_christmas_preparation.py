paper_roll = int(input())
plat_roll = int(input())
glue_litres = float(input())
discount_percent = int(input())

money = (paper_roll * 5.8) + (plat_roll * 7.2) + (glue_litres * 1.2)
real_money = money - ((money / 100) * discount_percent)
print(f"{real_money:.3f}")