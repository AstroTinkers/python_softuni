days_stay = int(input())
type_of_room = input()
review = input()
nights = days_stay - 1
price = 0
price_room = 18
price_ap = 25
price_pr = 35
if type_of_room == "room for one person":
    price = price_room
elif type_of_room == "apartment":
    price = price_ap
    if nights < 10:
        price *= 0.7
    elif 10 <= nights and nights <= 15:
        price *= 0.65
    elif nights > 15:
        price *= 0.5
elif type_of_room == "president apartment":
    price = price_pr
    if nights < 10:
        price *= 0.9
    elif 10 <= nights and nights <= 15:
        price *= 0.85
    elif nights > 15:
        price *= 0.8
if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.9
final_sum = price * nights
print(f"{final_sum:.2f}")