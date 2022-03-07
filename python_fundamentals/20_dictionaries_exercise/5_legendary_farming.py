def weapon(material):
    return {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}[material]


dict_mats = {'shards': 0, 'fragments': 0, 'motes': 0}
more_mats = True
while more_mats:
    materials = input().split(" ")
    for i in range(0, len(materials), 2):
        dict_mats.setdefault(materials[i + 1].lower(), 0)
        dict_mats[materials[i + 1].lower()] += int(materials[i])
        if dict_mats['shards'] >= 250 or dict_mats['fragments'] >= 250 or dict_mats['motes'] >= 250:
            more_mats = False
            break
legendary_weapon = [key for key, value in dict_mats.items() if value >= 250]
print(f"{weapon(legendary_weapon[0])} obtained!")
dict_mats[legendary_weapon[0]] -= 250
for key, value in dict_mats.items():
    print(f"{key}: {value}")
