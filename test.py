cells = [c.split(" = ") for c in input().split("#")]
cells = [(c[0], int(c[1])) for c in cells]
water = int(input())
fire_limits = {'High': (81, 125), 'Medium': (51, 80), 'Low': (1, 50)}

effort = 0
fire = 0
extinguished_cells = []

for (cell_type, level) in cells:
    if water <= 0:
        break
    if level > water:
        continue
    if level < fire_limits[cell_type][0] or level > fire_limits[cell_type][1]:
        continue
    water -= level
    effort += level * 0.25
    fire += level
    extinguished_cells.append(level)

print("Cells:")
for cell_level in extinguished_cells:
    print(f" - {cell_level}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")