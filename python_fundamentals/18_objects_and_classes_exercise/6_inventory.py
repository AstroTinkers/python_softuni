class Inventory:
    __capatity = 0

    def __init__(self, __capacity: int):
        Inventory.__capatity = __capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < Inventory.__capatity:
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return Inventory.__capatity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.__capatity - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
