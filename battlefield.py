from fleet import Fleet
from herd import Herd
import random

class Battlefield:

    
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

        
    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.display_welcome()
        self.battle()


    def display_welcome(self):
        print("Welcome to the thunderdome")

    def battle(self):
        self.battle_ongoing = True
        while self.battle_ongoing == True:
        
            if len(self.herd.dinosaurs) == 0:
                self.display_winners()

            elif len(self.fleet.robots) == 0:
                self.display_winners()

            elif self.herd.dinosaurs[0].health <= 0:
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
            
            elif self.fleet.robots[0].health <= 0:
                self.fleet.robots.remove(self.fleet.robots[0])

            elif self.herd.dinosaurs[0].health >= 0:
                self.dino_turn(random.choice(self.herd.dinosaurs))
            
            elif self.fleet.robots[0].health >= 0:
                self.robo_turn(random.choice(self.fleet.robots))

            else:
                print("Error")

    def dino_turn(self, dinosaur):
        self.dino_attack = dinosaur
        dinosaur.attack(random.choice(self.fleet.robots))


        if self.fleet.robots[0].health >= 0:
            self.robo_turn(random.choice(self.fleet.robots))
        
        else:
            self.battle()

    def robo_turn(self, robot):
        self.robo_attack = robot
        robot.attack(random.choice(self.herd.dinosaurs))

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponant_options(self):
        pass

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print("Robots win!!!")
            self.battle_ongoing = False

        elif len(self.fleet.robots) == 0:
            print("Dinosaurs win!!!")
            self.battle_ongoing = False

        else:
            print("Error")
