from weapon import Weapon

class Robot:
    def __init__(self, Name):
        self.name = Name
        self.health = 100
        self.weapon = Weapon("machine_gun", 20)

    def attack(self, Dinosaur):
        self.dinosaur = Dinosaur