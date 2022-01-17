budget = float(input())
season = input()

if budget <= 1000:
    attendance = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget and budget <= 3000:
    attendance = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.6
elif budget > 3000:
    attendance = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.9
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.9

print(f"{location} - {attendance} - {price:.2f}")