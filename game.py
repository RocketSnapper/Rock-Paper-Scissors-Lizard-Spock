from player import Player
from computer import Computer

class Game:
    def __init__(self):
        self.player_one = Player('Bill')
        self.player_two = Player('Jack')

    def run_game(self):
        self.display_rules()
        self.choose_opponent()
        Player.choose_gesture(self)

    def display_rules(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')
        print('RPSLS Rules')
        print('Rock beats Scissors and Lizard')
        print('Paper beats Rock and Spock')
        print('Scissors beats Paper and Lizard')
        print('Lizard beats Paper Spock')
        print('Spock beats Rock and Scissors')
        print(self.player_two.chosen_gesture)

    def choose_opponent(self):
        opponent_choice = int(input('Will there be 1 or 2 players?'))
        if opponent_choice == 1:
            self.player_two = Computer('Tim')
            Computer.randomize_gesture(self.player_two)
           
