def order_price(order, quantity):
    if order == "coffee":
        return quantity * 1.5
    elif order == "coke":
        return quantity * 1.4
    elif order == "water":
        return quantity * 1
    else:
        return quantity * 2


command, number = input(), float(input())
print(f"{order_price(command, number):.2f}")
