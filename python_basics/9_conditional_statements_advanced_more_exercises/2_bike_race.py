juniors = int(input())
seniors = int(input())
trail_type = input()

if trail_type == "trail":
    tax = juniors * 5.5 + seniors * 7
elif trail_type == "cross-country":
    tax = juniors * 8 + seniors * 9.5
elif trail_type == "downhill":
    tax = juniors * 12.25 + seniors * 13.75
elif trail_type == "road":
    tax = juniors * 20 + seniors * 21.5

if trail_type == "cross-country" and juniors + seniors >= 50:
    tax *= 0.75

final_sum = tax * 0.95
print(f"{final_sum:.2f}")