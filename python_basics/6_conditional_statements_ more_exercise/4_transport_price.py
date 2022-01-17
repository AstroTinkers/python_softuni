km = int(input())
time = str(input())

if time == "day":
    taxi_price = 0.7 + km * 0.79
else:
    taxi_price = 0.7 + km * 0.9

if km >= 20:
    bus_price = km * 0.09

if km >= 100:
    train_price = km * 0.06

if km < 20:
    print(f"{taxi_price:.2f}")
elif 20 <= km and km < 100 and bus_price > taxi_price:
    print(f"{taxi_price:.2f}")
elif 20 <= km and km < 100 and bus_price < taxi_price:
    print(f"{bus_price:.2f}")
elif 20 <= km and km >= 100 and bus_price > taxi_price and taxi_price < train_price:
    print(f"{taxi_price:.2f}")
elif 20 <= km and km >= 100 and taxi_price > bus_price and bus_price < train_price:
    print(f"{bus_price:.2f}")
else:
    print(f"{train_price:.2f}")