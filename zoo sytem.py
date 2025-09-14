from abc import ABC, abstractmethod

class Creature(ABC):

    def __init__(self, nm, yrs, hp):
        self.name = nm
        self.age = yrs
        self.__health = 0
        self.health = hp
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, val):
        if 0 <= val <= 100:
            self.__health = val
        else:
            print("Invalid health value!")
    @abstractmethod
    def make_sound(self):
        pass
    def eat(self):
        print(f"{self.name} is having food")
    def sleep(self):
        print(f"{self.name} is now sleeping")
class Mammal(Creature):
    pass
class Bird(Creature):
    pass
class Reptile(Creature):
    pass
class Lion(Mammal):
    def make_sound(self):
        print("ROAR!!")
class Elephant(Mammal):
    def make_sound(self):
        print("PRRRRR!")
class Penguin(Bird):
    def make_sound(self):
        print("Honk honk")
class Parrot(Bird):
    def make_sound(self):
        print("Hello! Squawk!")
class Snake(Reptile):
    def make_sound(self):
        print("Hissss")
class Worker:
    def __init__(self, nm):
        self.name = nm
class Vet(Worker):
    def heal(self, animal):
        print(self.name, "is checking", animal.name)
        animal.health = min(100, animal.health + 12)
class Keeper(Worker):
    def feed_animal(self, animal):
        print(self.name, "gives food to", animal.name)
        animal.eat()
    def transfer(self, animal, new_place):
        new_place.add_animal(animal)
        print(self.name, "moved", animal.name, "to", new_place.name)
class Habitat:
    def __init__(self, nm):
        self.name = nm
        self.animals = []
    def add_animal(self, ani):
        self.animals.append(ani)
    def __add__(self, other):
        merged = Habitat(self.name + "+" + other.name)
        merged.animals = self.animals + other.animals
        return merged
    def __len__(self):
        return len(self.animals)
class Hybrid(Mammal, Bird):
    def make_sound(self):
        print("Weird mix sound!")

    @classmethod
    def born(cls, nm):
        return cls(nm, 0, 100)
    @staticmethod
    def valid_species(sp):
        return sp in ["Lion", "Elephant", "Penguin", "Parrot","Snake"]
class Zoo:
    def __init__(self):
        self.places = []
        self.staff = []
    def add_place(self, plc):
        self.places.append(plc)
    def hire(self, emp):
        self.staff.append(emp)
    def __str__(self):
        return f"Zoo has {len(self.places)} habitats and {len(self.staff)} staff members"
if __name__ == "__main__":
    h1 = Habitat("Savannah")
    h2 = Habitat("BirdCage")
    h3 = Habitat("SnakePit")
    simba = Lion("Simba", 5, 88)
    dumbo = Elephant("Dumbo", 9, 79)
    pingu = Penguin("Pingu", 3, 83)
    polly = Parrot("Polly", 2, 96)
    nagini = Snake("Nagini", 4, 70)
    h1.add_animal(simba)
    h1.add_animal(dumbo)
    h2.add_animal(pingu)
    h2.add_animal(polly)
    h3.add_animal(nagini)
    myzoo = Zoo()
    myzoo.add_place(h1)
    myzoo.add_place(h2)
    myzoo.add_place(h3)
    doctor = Vet("Dr. Kareem")
    keeper = Keeper("Ahmed")
    myzoo.hire(doctor)
    myzoo.hire(keeper)
    doctor.heal(nagini)
    keeper.feed_animal(simba)
print(myzoo)
