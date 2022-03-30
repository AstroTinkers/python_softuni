class Dragon:
    def __init__(self, dragon_line):
        self.type, self.name, self.dmg, self.health, self.armor = dragon_line.split()
        self.dmg = 45 if self.dmg == 'null' else int(self.dmg)
        self.health = 250 if self.health == 'null' else int(self.health)
        self.armor = 10 if self.armor == 'null' else int(self.armor)

    def __repr__(self):
        return f"-{self.name} -> damage: {self.dmg}, health: {self.health}, armor: {self.armor}"

    def __eq__(self, other):
        return self.type == other.type and self.name == other.name


given_dragons = int(input())
dragons = []
for info in range(given_dragons):
    dragon_info = input()
    dragon_temp = Dragon(dragon_info)
    if dragon_temp in dragons:
        dragon_index = dragons.index(dragon_temp)
        dragons[dragon_index] = dragon_temp
    else:
        dragons.append(dragon_temp)
dragon_types = {}
for dragon in dragons:
    dragon_types.setdefault(dragon.type, [])
    dragon_types[dragon.type].append(dragon)
dragon_types = {d_type: sorted(drs, key=lambda x: x.name) for d_type, drs in dragon_types.items()}
for drg_type in dragon_types:
    avg_health, avg_armor, avg_dmg = 0, 0, 0
    len_dragon = len(dragon_types[drg_type])
    for d in dragon_types[drg_type]:
        avg_health += d.health
        avg_armor += d.armor
        avg_dmg += d.dmg
    avg_health /= len_dragon
    avg_armor /= len_dragon
    avg_dmg /= len_dragon
    print(f"{drg_type}::({avg_dmg:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for value in dragon_types[drg_type]:
        print(value)
