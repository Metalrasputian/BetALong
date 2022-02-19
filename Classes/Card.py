from dataclasses import dataclass

@dataclass
class Card:
    value: int
    rank: str
    suit: str
    isFaceUp: bool

    def __init__ (self, value, suit):
        self.value = value
        self.suit = suit
        self.isFaceUp = False
        self.rank = str(value)       
        
        if (value == 1):
            self.rank = "ace"
            value = 11
        elif (value == 11):
            self.rank = "jack"
        elif (value == 12):
            self.rank = "queen"
        elif (value == 13):
            self.rank = "king"

        if(value > 10):
            self.value = 10
    
    def aceToggle(self):
        if (self.rank == "ace"):
            if (self.value == 1):
                self.value = 11
            elif (self.value == 11):
                self.value = 1

    def getName(self):
        return self.rank + " of " + self.suit