from player import Player
import random

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def randomize_gesture(self):
        self.chosen_gesture = random.choice(self.gesture)
        
