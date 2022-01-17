budget = float(input())
gcards = int(input())
processors = int(input())
ram = int(input())

gcards_bought = gcards * 250
processor_price = gcards_bought * 0.35
ram_price = gcards_bought * 0.10
final_price = gcards_bought + (processor_price * processors) + (ram_price * ram)
if gcards > processors:
    final_price = (gcards_bought + (processor_price * processors) + (ram_price * ram)) * 0.85

difference = budget - final_price

if budget >= final_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva more!")