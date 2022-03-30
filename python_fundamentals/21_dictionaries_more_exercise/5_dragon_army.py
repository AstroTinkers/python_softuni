def add_dragon(type, stat, data):
    d_type, d_stat, d_damage, d_health, d_armor = data.split()
    if d_damage == 'null':
        d_damage = 45
    else:
        d_damage = int(d_damage)
    if d_health == 'null':
        d_health = 250
    else:
        d_health = int(d_health)
    if d_armor == 'null':
        d_armor = 10
    else:
        d_armor = int(d_armor)
    type[d_stat] = d_type
    stat[d_stat] = [d_damage, d_health, d_armor]


def average_stats(type, stats):
    damage = 0
    health = 0
    armor = 0
    for key1, value1 in type.items():
        for key in stats[value1]:
            damage += value[0]
            health += value[1]
            armor += value[2]
        break
    damage = damage / len(stats)
    health = health / len(stats)
    armor = armor / len(stats)
    return f"{damage:.2f}, {armor:.2f}, {health:.2f}"


dragons = {}
stats = {}
dragons_count = int(input())
for dragon in range(dragons_count):
    dragons_input = input()
    add_dragon(dragons, stats, dragons_input)
for dragon_type in dragons.keys():
    print(dragons[dragon_type])
    # avg_dmg, avg_health, avg_armor = average_stats(dragons, stats).split(", ")
    # print(f"{dragon_type}::({avg_dmg}/{avg_health}/{avg_armor})")
    # for stats[dragon_type]:
    print(f"-{dragon_type} -> damage: {stats[dragon_type][0]}, health: {stats[dragon_type][1]}, armor: {stats[dragon_type][2]}")
