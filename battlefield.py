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
        self.display_welcome


    def display_welcome(self):
        print("Welcome to the thunderdome")

    def battle(self):
        
        self.dino_turn(random.choice(self.herd.dinosaurs))
        self.robo_turn(self.fleet.robots[0])

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        print("test1")
        pass

    def show_robo_opponant_options(self):
        print("test2")
        pass

    def display_winners(self):
        pass