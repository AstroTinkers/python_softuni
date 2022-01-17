orders = int(input())
total = 0

for i in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsule_count = int(input())
    price = (capsule_price * capsule_count) * days
    total += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total:.2f}")