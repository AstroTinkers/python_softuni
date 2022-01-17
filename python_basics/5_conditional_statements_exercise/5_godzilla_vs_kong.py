budget = float(input())
extras = int(input())
clothing_price = float(input())

decor = budget * 0.10

wardrobe = extras * clothing_price
if extras > 150:
    wardrobe = (extras * clothing_price) * 0.9

difference = budget - (wardrobe + decor)

if budget >=(wardrobe + decor):
    print("Action!")
    print(f"Wingard starts filming with {abs(difference):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(difference):.2f} leva more.")
