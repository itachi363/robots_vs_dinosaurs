from weapon import Weapon

class Robot:
    def __init__(self, Name):
        self.name = Name
        self.health = 0
        self.weapon = Weapon

    def attack(self, Dinosaur):
        self.dinosaur = Dinosaur