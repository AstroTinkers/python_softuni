class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, type):
        if species == "mammal":
            zoo.mammals.append(type)
        elif species == "fish":
            zoo.fishes.append(type)
        elif species == "bird":
            zoo.birds.append(type)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        if species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo = Zoo(input())
zoo_animals = int(input())
for i in range(zoo_animals):
    animal = input().split(" ")
    species = animal[0]
    type = animal[1]
    zoo.add_animal(species, type)
animal_type = input()
print(zoo.get_info(animal_type))
