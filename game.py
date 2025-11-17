from player import Player
from computer import Computer

class Game:
    def __init__(self):
        self.player_one = Player('Bill')
        self.player_two = Player('Jack')

    def run_game(self):
        self.display_rules()

    def display_rules(self):
        print('RPSLS Rules')
        print('Rock beats Scissors and Lizard')
        print('Paper beats Rock and Spock')
        print('Scissors beats Paper and Lizard')
        print('Lizard beats Paper Spock')
        print('Spock beats Rock and Scissors')