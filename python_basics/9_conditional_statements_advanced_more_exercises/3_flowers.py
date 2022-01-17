hrizantemi = int(input())
roses = int(input())
laleta = int(input())
season = input()
holiday = input()

if season == "Spring" or season == "Summer":
    price_h = 2
    price_r = 4.1
    price_l = 2.5
elif season == "Autumn" or season == "Winter":
    price_h = 3.75
    price_r = 4.5
    price_l = 4.15

if holiday == "Y":
    price_h *= 1.15
    price_r *= 1.15
    price_l *= 1.15

bucket = hrizantemi * price_h + roses * price_r + laleta * price_l

if season == "Spring" and laleta > 7:
    bucket *= 0.95
if season == "Winter" and roses >= 10:
    bucket *= 0.9
if laleta + roses + hrizantemi > 20:
    bucket *= 0.8
final_bucket = bucket + 2
print(f"{final_bucket:.2f}")