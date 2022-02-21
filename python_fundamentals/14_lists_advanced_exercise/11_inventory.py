def collect(item, inventory):
    if item not in inventory:
        inventory.append(item)
    return inventory


def drop(item, inventory):
    if item in inventory:
        inventory.remove(item)
    return inventory


def combine(old_item, new_item, inventory):
    if old_item in inventory:
        inventory.insert(inventory.index(old_item) + 1, new_item)
    return inventory


def renew(item, inventory):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)
    return inventory


inventory_list = input().split(", ")
command = input()
while command != "Craft!":
    instruction, item = command.split(" - ")
    if instruction == "Collect":
        inventory_list = collect(item, inventory_list)
    elif instruction == "Drop":
        inventory_list = drop(item, inventory_list)
    elif instruction == "Combine Items":
        item = item.split(":")
        old_item, new_item = item
        inventory_list = combine(old_item, new_item, inventory_list)
    elif instruction == "Renew":
        inventory_list = renew(item, inventory_list)
    command = input()
print(", ".join(inventory_list))

