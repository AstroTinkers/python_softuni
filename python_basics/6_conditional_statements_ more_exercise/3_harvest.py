from math import floor
from math import ceil
sqm_loze = int(input())
grape_per_sqm = float(input())
l_wine_needed = int(input())
workers = int(input())
wine = ((sqm_loze * grape_per_sqm) / 2.5) * 0.4
difference = abs(wine - l_wine_needed)
wine_per_worker = difference / workers
if wine >= l_wine_needed:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")