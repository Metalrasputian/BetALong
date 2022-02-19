from dataclasses import dataclass
from msilib.schema import SelfReg

from Classes.Card import Card
from Classes.Deck import Deck

@dataclass
class Dealer:
    deck: Deck
    hand: list

    def deal(self, target, faceUp = True):
        card = self.deck.draw()
        card.isFaceUp = faceUp
        target.hand.append(card)

    def ask(self, player):
        decision = player.decice()

        if decision == "hit":
            self.deal(player)
    
    def __init__(self, deckCount):
        self.deck = Deck(deckCount)
        self.hand = list()