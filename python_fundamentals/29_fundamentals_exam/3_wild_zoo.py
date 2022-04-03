animals_food = {}
animals_area = {}
input_data = input()
while not input_data == "EndDay":
    input_data = input_data.split(":")
    input_data[1] = input_data[1].split("-")
    if input_data[0] == "Add":
        animals_food.setdefault(input_data[1][0], 0)
        animals_food[input_data[1][0]] += int(input_data[1][1])
        animals_area.setdefault(input_data[1][2], [])
        if input_data[1][0] not in animals_area[input_data[1][2]]:
            animals_area[input_data[1][2]].append(input_data[1][0])
    else:
        if input_data[1][0] in animals_food:
            animals_food[input_data[1][0]] -= int(input_data[1][1])
            if animals_food[input_data[1][0]] <= 0:
                print(f"{input_data[1][0]} was successfully fed")
                animals_food.pop(input_data[1][0])
                for area, animal in animals_area.items():
                    if input_data[1][0] in animal:
                        animal.pop(animal.index(input_data[1][0]))
    input_data = input()
print("Animals:")
for animal in animals_food:
    print(f"{animal} -> {animals_food[animal]}g")
print("Areas with hungry animals:")
for area in animals_area:
    if len((animals_area[area])) > 0:
        print(f"{area}: {len(animals_area[area])}")
