budget = float(input())
flour_price = float(input())
milk_price = flour_price * 1.25
egg_price = flour_price * 0.75
bread_price = flour_price + milk_price * 0.25 + egg_price
breads_made = 0
eggs_received = 0
while budget >= bread_price:
    budget -= bread_price
    breads_made += 1
    eggs_received += 3
    if breads_made % 3 == 0:
        eggs_received -= breads_made - 2
print(f"You made {breads_made} loaves of Easter bread! Now you have {eggs_received} eggs and {budget:.2f}BGN left.")