price_t_shirt = float(input())
money_ball = float(input())

shorts = price_t_shirt * 0.75
socks = shorts * 0.2
buttonki = 2 * (price_t_shirt + shorts)

price =(price_t_shirt + shorts + socks + buttonki) * 0.85
difference = money_ball - price
if price >= money_ball:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {price:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")