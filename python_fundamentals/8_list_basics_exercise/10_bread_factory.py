events = input().split("|")
energy = 100
coins = 100
made_it_through = True
for i in events:
    number = int(i.split("-")[1])
    if i.startswith("rest"):
        if energy + number > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif i.startswith("order"):
        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {i.split('-')[0]}.")
        else:
            print(f"Closed! Cannot afford {i.split('-')[0]}.")
            made_it_through = False
            break
if made_it_through:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")