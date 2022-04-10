# exerceise 1
import bark as bark


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


mike = Cat("mike", 1)
jason = Cat("jason", 2)
albert = Cat("albert", 3)

cat_list = [Cat("mike", 1), Cat("jason", 2), Cat("albert", 3)]

oldestCat = cat_list[0]
for oneCat in cat_list:
    if oneCat.age > oldestCat.age:
        oldestCat = oneCat

print(oldestCat.name, oldestCat.age, sep=" ")

print(f"the oldest cat is {oldestCat.name}, and is {oldestCat.age} years old.")


# exercise 2

class Dog:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof')

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("rex", 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height < davids_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)


# exercise 3

class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(self.lyrics)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# exercise 4

class Zoo:

    def __init__(self, zoo_name):
        self.animals = ([])
        self.zoo_name = zoo_name

    def add_animal(self, new_animal):
        new_animal += self.animals

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        animal_sold -= self.animals

    def sort_animals(self):
        self.animals.sort()


