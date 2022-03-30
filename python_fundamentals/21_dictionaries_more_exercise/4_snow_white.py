def add_dwarf(dwarf_line: str, dwarves: dict):
    dwarf_name, dwarf_hat, dwarf_physics = dwarf_line.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    if dwarf_hat in dwarves:
        if dwarf_name in dwarves[dwarf_hat]:
            dwarves[dwarf_hat][dwarf_name] = max(dwarf_physics, dwarves[dwarf_hat][dwarf_name])
        else:
            dwarves[dwarf_hat][dwarf_name] = dwarf_physics
    else:
        dwarves[dwarf_hat] = {dwarf_name: dwarf_physics}


def sort_dwarves(dwarves: dict):
    list_1 = []
    for hat, name in dwarves.items():
        for k1, v1 in name.items():
            list_1.append([hat, k1, v1])
    list_1 = list(sorted(list_1, key=lambda y: (-y[2], y[0])))
    return list_1


dwarves_data = {}
input_data = input()
while not input_data == "Once upon a time":
    add_dwarf(input_data, dwarves_data)
    input_data = input()
dwarves_print = sort_dwarves(dwarves_data)
for dwarf in dwarves_print:
    print(f"({dwarf[0]}) {dwarf[1]} <-> {dwarf[2]}")
