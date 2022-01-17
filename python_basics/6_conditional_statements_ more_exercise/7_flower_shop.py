from math import floor, ceil
magnolii = int(input())
ziumbiuli = int(input())
roses = int(input())
kaktusi = int(input())
gift = float(input())
money = magnolii * 3.25 + ziumbiuli * 4 + roses * 3.5 + kaktusi * 8
money_final = money - (money * 0.05)
difference = abs(money_final - gift)
if money_final >= gift:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")