fuel_type = str(input())
litres = float(input())
card = str(input())
if fuel_type == "Gas" and card == "Yes":
    price = 0.93 - 0.08
if fuel_type == "Gas" and card == "No":
    price = 0.93
if fuel_type == "Gasoline" and card == "Yes":
    price = 2.22 - 0.18
if fuel_type == "Gasoline" and card == "No":
    price = 2.22
if fuel_type == "Diesel" and card == "Yes":
    price = 2.33 - 0.12
if fuel_type == "Diesel" and card == "No":
    price = 2.33
final = price * litres
if 20 <= litres and litres <= 25:
    final -= final * 0.08
if litres > 25:
    final -= final * 0.1
print(f"{final:.2f} lv.")

