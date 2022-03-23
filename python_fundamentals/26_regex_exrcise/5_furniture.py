import re
command = input()
total_sum = 0
pattern = r">>(?P<furniture>\w+)<<(?P<price>\d+\.?(\d+)?)!(?P<quantity>\d+)"
print(f"Bought furniture:")
while not command == "Purchase":
    valid_purchase = re.match(pattern, command)
    if valid_purchase:
        total_sum += float(valid_purchase.group('price')) * int(valid_purchase.group('quantity'))
        print(valid_purchase.group('furniture'))
    command = input()
print(f'Total money spend: {total_sum:.2f}')
