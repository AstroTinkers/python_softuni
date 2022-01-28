fire_type = input().split("#")
water = int(input())
effort = 0
total_fire = 0
print("Cells:")
for i in fire_type:
    fire_level = int(i.split()[2])
    if water >= fire_level:
        if i.startswith("High") and not 81 <= fire_level <= 125:
            continue
        elif i.startswith("Medium") and not 51 <= fire_level <= 80:
            continue
        elif i.startswith("Low") and not 1 <= fire_level <= 50:
            continue
    else:
        continue
    water -= fire_level
    total_fire += fire_level
    effort += fire_level * 0.25
    print(f" - {fire_level}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
