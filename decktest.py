from playingcard import*
from random import*

class Deck:
    def __init__(self):
        suits = ['d','s','h','c']
        self.cards = []
        for i in range(0,13):
            for suit in suits:
                self.cards.append(PlayingCard(i,suit))
        #print(len(self.cards))
        
    
    def shuffle(self):
        shuffle(self.cards)
        
    def dealCard(self):
        card = self.cards[-1]
        del self.cards[-1]
        return card

    def cardsLeft(self):
        return self.cards

def main():
    deck = Deck()
    deck.shuffle()
    for i in range(2):
        x = deck.dealCard()
        print(x)
        print(x.value())
if __name__ == "__main__":
    main()

