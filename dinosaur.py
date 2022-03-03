class Dinosaur:
    def __init__(self, Name, Attack_power):
        self.name = Name
        self.attack_power = int(Attack_power)
        self.health = 100

    def attack(self, Robot):
        self.robot = Robot