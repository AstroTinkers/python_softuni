package_weight = float(input())
service = input()
distance = int(input())
price_km =0
if package_weight < 1:
    price_km = 3
elif package_weight < 10:
    price_km = 5
elif package_weight < 40:
    price_km = 10
elif package_weight < 90:
    price_km = 15
elif package_weight < 150:
    price_km = 20

if service == "standard":
    price_final = distance * (price_km / 100)
else:
    if package_weight < 1:
        price_final = (distance * (price_km / 100)) + (distance * (((price_km / 100) * 0.8) * package_weight))
    elif package_weight < 10:
        price_final = (distance * (price_km / 100)) + (distance * (((price_km / 100) * 0.4) * package_weight))
    elif package_weight < 40:
        price_final = (distance * (price_km / 100)) + (distance * (((price_km / 100) * 0.05) * package_weight))
    elif package_weight < 90:
        price_final = (distance * (price_km / 100)) + (distance * (((price_km / 100) * 0.02) * package_weight))
    elif package_weight < 150:
        price_final = (distance * (price_km / 100)) + (distance * (((price_km / 100) * 0.01) * package_weight))

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {price_final:.2f} lv.")