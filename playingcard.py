
class PlayingCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if 10 <= self.rank <= 13:
            return 10
        else:
            return self.rank + 1

    def __str__(self):
        n = self.rank
        rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = {'d':'diamonds','s':'spades','h':'hearts','c':'clubs'}

        finalcard = rank[n] + ' of ' + suits[self.suit]
        
        return finalcard

def main():
    card = PlayingCard(8,'d')
    print(card)
    print(card.value())
if __name__ == '__main__':
    main()
