import itertools
from random import shuffle

class Deck():
    def __init__(self):
        self.deck = []

    def build(self, card, quantity):
        self.deck.extend(list(itertools.repeat(card, quantity)))

    def shuffle(self):
        shuffle(self.deck)

    def draw(self):
        return self.deck.pop(0)

