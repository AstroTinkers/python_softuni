class Dwarf:
    def __init__(self, dwarf_data):
        self.name, self.hat, self.physics = dwarf_data.split(" <:> ")
        self.physics = int(self.physics)

    def __repr__(self):
        return f"({dwarf.hat}) {dwarf.name} <-> {dwarf.physics}"

    def __eq__(self, other):
        return self.name == other.name and self.hat == other.hat


input_data = input()
dwarves = []
while not input_data == "Once upon a time":
    dwarf_temp = Dwarf(input_data)
    if dwarf_temp in dwarves:
        dwarf_index = dwarves.index(dwarf_temp)
        dwarves[dwarf_index].physics = max(dwarf_temp.physics, dwarves[dwarf_index].physics)
    else:
        dwarves.append(dwarf_temp)
    input_data = input()
dwarves_by_hat_color = {}
for dwarf in dwarves:
    dwarves_by_hat_color.setdefault(dwarf.hat, [])
    dwarves_by_hat_color[dwarf.hat].append(dwarf)
dwarves_sorted = [dwarf for dwarf in sorted(dwarves, key=lambda x: (x.physics, len(dwarves_by_hat_color[x.hat])),
                                            reverse=True)]
for dwarf in dwarves_sorted:
    print(dwarf)