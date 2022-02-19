from Classes.Dealer import Dealer
from Classes.Player import Player

class GameManager:
    
    def getScore(self, hand):
        cardSum = 0

        for card in hand:
            cardSum += card.value
        
        if card > 21:
            highAces = [x for x in hand if x.value == 11]

            if (len(highAces) > 0):
                hand[highAces[0]] = highAces[0].aceToggle()

    def placeBets(self):
        pass

    def dealCards(self):
        pass

    def initialDeal(self):
        for player in self.players:
            self.dealer.deal(player)
        
        self.dealer.deal(self.dealer)

        for player in self.players:
            self.dealer.deal(player)
        
        self.dealer.deal(self.dealer, False)

    def renderTable(self):
        for player in self.players:
            print (player.name)
            for card in player.hand:
                print(card.getName())

        print ("Dealer")

        for card in self.dealer.hand:
            message = card.getName()
            if(card.isFaceUp is False): 
                message += "**"
            print(message)

    
    def play(self):        

        self.players.append(Player("Bob"))

        self.dealer.deck.shuffle()

        self.placeBets()

        self.initialDeal()

        

        self.renderTable()
    
    def __init__(self, deckCount = 1):
        self.players = list()
        self.dealer = Dealer(deckCount)