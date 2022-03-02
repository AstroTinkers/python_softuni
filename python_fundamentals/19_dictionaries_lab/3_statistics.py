command = input()
product_list = {}
while command != "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product in product_list:
        product_list[product] += quantity
    else:
        product_list[product] = quantity
    command = input()
print("Products in stock:")
for item, count in product_list.items():
    print(f"- {item}: {count}")
print(f"Total Products: {len(product_list)}")
print(f"Total Quantity: {sum(product_list.values())}")
