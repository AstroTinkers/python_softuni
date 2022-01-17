months = int(input())
electric_bill = 0
water = 20 * months
internet = 15 * months
other = 0
for i in range(months):
    electricity = float(input())
    electric_bill += electricity
    other += (20 + 15 + electricity) * 1.2
average = (electric_bill + water + internet + other) / months
print(f"Electricity: {electric_bill:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")