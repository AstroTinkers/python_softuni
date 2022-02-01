events = input().split("|")
energy = 100
coins = 100
made_it_through = True
for i in events:
    event_parts = i.split("-")
    (event, number) = event_parts[0], int(event_parts[1])
    if event == "rest":
        if energy + number > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
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
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            made_it_through = False
            break
if made_it_through:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
