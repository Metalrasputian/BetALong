from dataclasses import dataclass
from Classes.Card import Card

@dataclass
class Player:
    runningCount : int
    wallet: int
    hand : list
    lastDecision : str
    name : str

    def countCard(self, card):
        if (card.value < 7):
            self.runningCount -= 1
        elif (card.value < 9):
            self.runningCount += 1
    
    def decide(self, score):
        decision = ""

        if score < 21:
            decision = "hit"
        else:        
            decision = "stay"

        return decision

    def __init__(self, name):
        self.name = name
        self.hand = list()
        self.lastDecision = ""
        self.runningCount = 0