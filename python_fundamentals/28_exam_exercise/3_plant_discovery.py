plants_rarity = {}
plants_rating = {}
plants_number = int(input())
for plant in range(plants_number):
    plant_given = input().split("<->")
    plants_rarity[plant_given[0]] = int(plant_given[1])
command = input()
while not command == "Exhibition":
    command = command.split()
    if command[1] not in plants_rarity:
        print("error")
    elif command[0] == "Rate:":
        plants_rating.setdefault(command[1], [])
        plants_rating[command[1]].append(int(command[3]))
    elif command[0] == "Update:":
        plants_rarity[command[1]] = int(command[3])
    else:
        plants_rating[command[1]].clear()
    command = input()
print("Plants for the exhibition:")
for plant in plants_rarity:
    avg_rarity = 0 if plant not in plants_rating or sum(plants_rating[plant]) == 0  else sum(plants_rating[plant]) / len(plants_rating[plant])
    print(f"- {plant}; Rarity: {plants_rarity[plant]}; Rating: {avg_rarity:.2f}")
