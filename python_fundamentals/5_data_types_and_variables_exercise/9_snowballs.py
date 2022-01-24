snowballs = int(input())
snowball_value = 0
perfect_weight = 0
perfect_time = 0
perfect_quality = 0
for i in range(1, snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_formula = int((snowball_weight / snowball_time) ** snowball_quality)
    if snowball_value < snowball_formula:
        snowball_value = snowball_formula
        perfect_weight = snowball_weight
        perfect_time = snowball_time
        perfect_quality = snowball_quality
print(f"{perfect_weight} : {perfect_time} = {snowball_value} ({perfect_quality})")
