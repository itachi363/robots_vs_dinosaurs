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
        
            if self.herd.dinosaurs[0].health <= 0:
                self.herd.dinosaurs.remove[0]
            
            elif self.fleet.robots[0].health <= 0:
                self.fleet.robots.remove[0]

            elif self.herd.dinosaurs[0].health >= 0:
                self.dino_turn(self.herd.dinosaurs[0].attack_power)
            
            elif self.fleet.robots[0].health >= 0:
                self.robo_turn(self.fleet.robots[0].weapoon.attack_power)

            elif len(self.herd.dinosaurs) == 0:
                self.display_winners()

            elif len(self.fleet.robots) == 0:
                self.display_winners()
            else:
                print("Error")

    def dino_turn(self, dinosaur):
        self.dino_attack = dinosaur
        dinosaur -= self.fleet.robots[0].health

        if self.fleet.robots[0].health >= 0:
            self.robo_turn(self.fleet.robots[0].weapon.attack_power)
        
        else:
            self.battle()

    def robo_turn(self, robot):
        self.robo_attack = robot
        robot -= self.herd.dinosaurs[0].health

    def show_dino_opponent_options(self):
        print("test1")
        pass

    def show_robo_opponant_options(self):
        print("test2")
        pass

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            self.battle_ongoing == False
            print("Robots win!!!")

        elif len(self.fleet.robots) == 0:
            self.battle_ongoing == False
            print("Dinosaurs win!!!")

        else:
            print("Error")