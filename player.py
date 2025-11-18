class Player:
    def __init__(self, name):
        self.gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.name = name
        self.score = 0
        self.chosen_gesture = None

    def choose_gesture(self):
        self.chosen_gesture = input('Choose a gesture for your next turn:')
        print(self.chosen_gesture)
    