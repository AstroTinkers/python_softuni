import math
events = input().split("|")

energy = 100
coins = 100

for event in events:
    event_parts = command.split("-")
    (command, value) = event_parts[0], int(event_parts[1])
    if command == "rest":
        old_energy = energy
        new_energy = min(100, energy + value)
        energy = new_energy
        outcome = ("rest", old_energy, new_energy)
    elif command == "order":
        if energy < 30:
            energy += 50
            outcome = ("rest_forced")
        else:
            energy -= 30
            outcome = ("coin_increase", coins, coins + value)
            coins += value
    else:
        if coins >= value:
            coins -= value
            outcome = ("purchase_success", command)
        else:
            outcome = ("purchase_fail", command)

    if outcome[0] == "rest":
        print(f"You gained {outcome[1]} energy")
        print(f"Current energy: {energy}")
    elif outcome[0] == "rest_forced":
        print("You had to rest!")
    elif outcome[0] == "coin_increase":
        print(f"You earned {outcome[1]} coins")