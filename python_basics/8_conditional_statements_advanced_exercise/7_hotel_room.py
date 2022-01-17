month = input()
nights = int(input())
price_studio = 0
price_apartment = 0
if month == "May" or month == "October":
    price_studio = 50
    if nights > 7 and nights <= 14:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.7
    price_apartment = 65
elif month == "June" or month == "September":
    price_studio = 75.20
    if nights > 14:
        price_studio *= 0.8
    price_apartment = 68.70
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

if nights > 14:
    price_apartment *= 0.9
stay_apartment = price_apartment * nights
stay_studio = price_studio * nights
print(f"Apartment: {stay_apartment:.2f} lv.")
print(f"Studio: {stay_studio:.2f} lv.")