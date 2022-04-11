class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, name, amount=1):
        if name in self.animals:
            self.animals[name] += amount
        else:
            self.animals[name] = amount

    def get_info(self):
        for animal, amount in self.animals.items():
            print(f"{animal} : {amount}")

    def get_animal_types(self):
        types = list(self.animals.keys())
        types.sort()
        return types


mcdonald = Farm("McDonald")
mcdonald.add_animal("cow", 5)
mcdonald.add_animal("goat", 3)
mcdonald.add_animal("sheep")
mcdonald.add_animal("sheep")

print(mcdonald.name)
mcdonald.get_info()
print(mcdonald.get_animal_types())
