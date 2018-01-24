from deck import Deck

class Player():
    def __init__(self, name):
        self.name = name
        self.successes = 0
        self.failures = 0

    def take_turn(self):
        print('wait for input')
        print('take action')

class Game():
    def __init__(self, players)
        self.players = players
        self.deck = Deck()

    def round(self):
        build_deck()
        while self.players.size() > 1:
            for player in self.players:
                player.take_turn()

    def build_deck(self):
        for k, v in monsters.items():
            deck.build(k, v['quantity'])
        deck.shuffle()

