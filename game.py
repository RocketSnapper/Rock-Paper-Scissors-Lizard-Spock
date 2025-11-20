from player import Player
from computer import Computer

class Game:
    def __init__(self):
        self.player_one = Player('Bill')
        self.player_two = Player('Jack')

    def run_game(self):
        self.display_rules()
        self.choose_opponent()
        self.round_phase()
        self.declare_winner()

    def display_rules(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')
        print('RPSLS Rules')
        print('Rock beats Scissors and Lizard')
        print('Paper beats Rock and Spock')
        print('Scissors beats Paper and Lizard')
        print('Lizard beats Paper Spock')
        print('Spock beats Rock and Scissors')

    def choose_opponent(self):
        opponent_choice = (input('Will there be 1 or 2 players?'))
        if opponent_choice == '1':
            self.player_two = Computer('Tim')
            Computer.randomize_gesture(self.player_two)
        elif opponent_choice == '2':
            opponent_choice = '2'
        else:
            print('Incorrect entry, try again')
            self.choose_opponent()

    def round_phase(self):

        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            #rework for when computer is used, dont need a second choose gesture here for that
            if self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture in ['Scissors', 'Lizard']:
                print('Player one wins this round')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture in ['Rock', 'Spock']:
                print('Player one wins this round')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture in ['Paper', 'Lizard']:
                print('Player one wins this round')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture in ['Paper', 'Spock']:
                print('Player one wins this round')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture in ['Rock', 'Scissors']:
                print('Player one wins this round')
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                self.player_one.chosen_gesture = self.player_two.chosen_gesture
                print('Both players chose the same gesture, keep playing!')
            else:
                self.player_two.score += 1
                print('Player two wins this round')
    
            

    def declare_winner(self):
        if self.player_one.score == 2:
            print(f'{self.player_one.name} wins the game')
        else:
            print(f'{self.player_two.name} wins the game')

           
