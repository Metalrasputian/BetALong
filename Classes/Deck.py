from dataclasses import dataclass
from Classes.Card import Card
import random

@dataclass
class Deck:

    cards: list

    def __init__(self, count = 1):
        for deckCount in range(count):
            for suit in ["clubs", "spades", "hearts", "diamonds"]:
                for i in range(1, 13):
                    self.cards.append(Card(i, suit))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card