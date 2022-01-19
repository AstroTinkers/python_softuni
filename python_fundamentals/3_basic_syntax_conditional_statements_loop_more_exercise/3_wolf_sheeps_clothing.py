animals = input()
animals_queue = animals.split(", ")
if animals_queue[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    predator = "wolf"
    print(f"Oi! Sheep number {len(animals_queue) - animals_queue.index(predator) - 1}! You are about to be "
          f"eaten by a wolf!")
