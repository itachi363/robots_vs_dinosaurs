from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.attack = Dinosaur

    def create_herd(self):
        dinosaur_one = Dinosaur("Velociraptor", 20)
        self.dinosaurs.append(dinosaur_one)
        dinosaur_two = Dinosaur("T-Rex", 30)
        self.dinosaurs.append(dinosaur_two)
        dinosaur_three = Dinosaur("pterodactyl", 15)
        self.dinosaurs.append(dinosaur_three)
