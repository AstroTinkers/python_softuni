from math import floor, ceil
days_gone = int(input())
food = int(input())
f_dog = float(input())
f_cat = float(input())
f_turtle = float(input())

food_needed = f_dog * days_gone + f_cat * days_gone + ((f_turtle * days_gone) / 1000)
difference = abs(food - food_needed)

if food >= food_needed:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")