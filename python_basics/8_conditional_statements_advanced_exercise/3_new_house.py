flowers , f_quantity , budget = input() , int(input()) , int(input())
price = 0
if flowers == "Roses":
    price = 5
elif flowers == "Dahlias":
    price = 3.8
elif flowers == "Tulips":
    price = 2.8
elif flowers == "Narcissus":
    price = 3
elif flowers == "Gladiolus":
    price = 2.5

if flowers == "Roses" and f_quantity > 80:
    price *= 0.9
elif flowers == "Dahlias" and f_quantity > 90:
    price *= 0.85
elif flowers == "Tulips" and f_quantity > 80:
    price *= 0.85
elif flowers == "Narcissus" and f_quantity < 120:
    price *= 1.15
elif flowers == "Gladiolus" and f_quantity < 80:
    price *= 1.2
final_price = price * f_quantity
difference = abs(budget - final_price)
if budget >= final_price:
    print(f"Hey, you have a great garden with {f_quantity} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")