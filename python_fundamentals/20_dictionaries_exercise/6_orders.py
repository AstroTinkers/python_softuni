command = input()
stock = {}
while command != "buy":
    product, price, quantity = command.split(" ")
    stock.setdefault(product, [0, 0])
    stock[product][0] = float(price)
    stock[product][1] += int(quantity)
    command = input()
for key, value in stock.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
