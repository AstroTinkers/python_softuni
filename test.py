import re
command = input()
furniture_bought = {}
pattern = r">>(?P<furniture>\w+)<<(?P<price>\d*\.?\d+?)!(?P<quantity>\d+)"
while not command == "Purchase":
    valid_purchase = re.match(pattern, command)
    if valid_purchase and valid_purchase.group('furniture' and 'price' and 'quantity'):
        sum_of_purchase = float(valid_purchase.group('price')) * int(valid_purchase.group('quantity'))
        if sum_of_purchase > 0:
            furniture_bought.setdefault(valid_purchase.group('furniture'), 0)
            furniture_bought[valid_purchase.group('furniture')] += sum_of_purchase
    command = input()
print(f"Bought furniture:", *furniture_bought.keys(), sep="\n")
print(f'Total money spend: {sum(furniture_bought.values()):.2f}')