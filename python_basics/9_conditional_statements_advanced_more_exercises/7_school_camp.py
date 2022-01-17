season = input()
group_type = input()
students = int(input())
nights = int(input())

if season == "Winter":
    if group_type == "boys":
        price = 9.6
        sport = "Judo"
    elif group_type == "girls":
        price = 9.6
        sport = "Gymnastics"
    elif group_type == "mixed":
        price = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price = 7.2
        sport = "Tennis"
    elif group_type == "girls":
        price = 7.2
        sport = "Athletics"
    elif group_type == "mixed":
        price = 9.5
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "girls":
        price = 15
        sport = "Volleyball"
    elif group_type == "mixed":
        price = 20
        sport = "Swimming"
price_stay = price * nights * students
if 10 <= students and students < 20:
    price_stay *= 0.95
elif 20 <= students and students < 50:
    price_stay *= 0.85
elif students >= 50:
    price_stay *= 0.5

print(f"{sport} {price_stay:.2f} lv.")