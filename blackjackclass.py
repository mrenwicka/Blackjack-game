##from playingcard import*
##from decktest import*
##from random import*
##from graphics import*

#Brooke Brandenburger and Miles renwhich
#due date is 11-29-2022
#this program creates a functioning game of blackjack with the dealer and player and includes a graphic display

from playingcard import*
from decktest import*
from random import*
from graphics import*
#from time import*
from buttonforblackjack import*

class BlackJack:
    def __init__(self,dHand=[] ,pHand=[]):
        self.dealHand = dHand=[]
        self.personHand = pHand=[]
        self.deck = Deck()
        self.deck.shuffle()
        print(self.dealHand)
        print(self.personHand)

    def initDeal(self,myWin,xP, yP, xD, yD):
        for i in range(2):
            x = self.deck.dealCard()
            self.personHand.append(x)
            pCardDisplay=Image(Point(xP+125*i,yP), "playingcards/"+str(x.getSuit())+str(x.getRank())+".gif")
            pCardDisplay.draw(myWin)

        dealercard1=self.deck.dealCard()
        dealercard2=self.deck.dealCard()
        self.dealHand.append(dealercard1)
        self.dealHand.append(dealercard2)

        faceDownCard=Image(Point(xD,yD), "playingcards/b1fv.gif")
        dCardDisplay=Image(Point(xD+125,yD), "playingcards/"+str(dealercard2.getSuit())+str(dealercard2.getRank())+".gif")
        faceDownCard.draw(myWin)
        dCardDisplay.draw(myWin)

    def getHandP(self):
        return self.personHand
    def getHandD(self):
        return self.dealHand
    def hit(self,win,x,y):
        HitCard=self.deck.dealCard()
        self.personHand.append(HitCard)
        pHitCardImage=Image(Point(x,y), "playingcards/"+str(HitCard.getSuit())+str(HitCard.getRank())+".gif")
        hitCardImage.draw(win)
        
##    def evaluateHand(self,hand):
##        valueList=[]
##        for i in range(len(hand)):
##            valueList.append((hand[i].value()))
##            
##        val=0
##        for i in range(len(hand)):
##            appended=hand[i].value()
##            val+=appended
##            
##            if val<=11 and 1 in valueList:
##                val+=10
##        if val>21 and 1 in valueList:
##            val=val-10
##                    
##        return val
    def evaluateHand(self,hand):
        val = 0
        total = 0
        for i in range(len(hand)):
            if hand[i].getRank() == 1:
                val = val + 1
                total = total + 11

            elif hand[i].value() == 10:
                total = total + 10

            else:
                total = total + hand[i].getRank()

        while total > 21 and val > 0:
            total = total - 10
            val = val - 1
        return total
            
        
    
    def DealerPlays(self, win, x, y):
        total=0
        
        while self.evaluateHand(self.getHandD())<17:
            newDcard=self.deck.dealCard()
            self.dealHand.append(newDcard)

            dHitCardImage = Image(Point(x+100*total,y), "playingcards/"+str(newDcard.getSuit())+str(newDcard.getRank())+".gif")
            dHitCardImage.draw(win)
            total+=1
        show=Image(Point(250, 100), "playingcards/"+str(self.getHandD()[0].getSuit())+str(self.getHandD()[0].getRank())+".gif")
        show.draw(myWin)

def main():

    
    myWin=GraphWin('black jack',800,800)
    myWin.setBackground("darkorchid1")
    
    intro=Text(Point(400,125),"Welcome to Miles and Brooke's \n Ca$ino")
    intro.setStyle("bold")
    intro.setSize(45)
    intro.draw(myWin)
    intro2=Text(Point(404,129),"Welcome to Miles and Brooke's \n Ca$ino")
    intro2.setStyle("bold")
    intro2.setSize(45)
    intro2.setFill("white")
    intro2.draw(myWin)
    intro3=Text(Point(400,640),"Press start to play Blackjack")
    intro3.setStyle("bold")
    intro3.setFill("white")
    intro3.setSize(45)
    intro3.draw(myWin)
    intro4=Text(Point(402,642),"Press start to play Blackjack")
    intro4.setStyle("bold")
    intro4.setSize(45)
    intro4.draw(myWin)

    casino = Image(Point(400,390), "casinoImage.png")
    casino.draw(myWin)

    startButton=Button(myWin,Point(400,725), 100, 50, "Start")
    startButton.activate()
    quitButton=Button(myWin,Point(730,725), 100, 50, "Quit")
    quitButton.activate()
    

    
    pt=myWin.getMouse()
    while not quitButton.clicked(pt):
            if startButton.clicked(pt):
                casino.undraw()
                intro.undraw()
                intro2.undraw()
                intro3.undraw()
                intro4.undraw()

                myWin.setBackground("grey30")

                ruleintro=Text(Point(400,100),"Rules of Blackjack")
                ruleintro.setStyle("bold")
                ruleintro.setFill("black")
                ruleintro.setSize(45)
                ruleintro.draw(myWin)
                rules=Text(Point(400,350),"1. players go agaisnt the dealer \n and try to get as close to 21 \n without going over which is a bust \n 2. player is dealt two cards and \n can either hit or stand \n 3. an ace is either worth 1 or 11 \n 4. all face cards are 10 \n 5. the dealers first card is facedown")
                rules.setStyle("bold")
                rules.setFill("white")
                rules.setSize(30)
                rules.draw(myWin)
                
                playbtn=Text(Point(400,550),"click anywhere to start game")
                playbtn.setStyle("bold")
                playbtn.setFill("black")
                playbtn.setSize(45)
                playbtn.draw(myWin)
                myWin.getMouse()

                ruleintro.undraw()
                rules.undraw()
                playbtn.undraw()
                startButton.deactivate()
                deck = Deck()
                deck.shuffle()

                pHand = [deck.dealCard(),deck.dealCard()]
                dHand = [deck.dealCard()]
                startgame=BlackJack(dHand,pHand)

                
##                #self.dHand
##                dealercard1=self.deck.dealCard()
##                dealercard2=self.deck.dealCard()
##                self.dHand.append(dealercard1)
##                self.dHand.append(dealercard2)
##
##                x = self.deck.dealCard()
##                self.pHand.append(x)
                

                hitButton=Button(myWin,Point(100,660), 100, 50, "Hit")
                StandButton = Button(myWin, Point(300,660), 100, 50, "Stand")
                hitButton.activate()
                StandButton.activate()
                print(startgame.getHandP())

                pScore=Text(Point(200,600),f'players hand value: {startgame.evaluateHand(startgame.getHandP())}')
                pScore.setStyle("bold")
                pScore.setFill("black")
                pScore.setSize(37)
                pScore.draw(myWin)
                dScore=Text(Point(200,300),"dealers hand value: ")
                dScore.setStyle("bold")
                dScore.setFill("black")
                dScore.setSize(37)
                dScore.draw(myWin)

                startgame.initDeal(myWin, 250, 400, 250, 100)

                if hitButton.clicked(pt):
                    startgame.hit(win, 250+100*len(play.getHandP()), 400)
                    #I place the new cards at a distance from the initial proportional to the size of the hand
                    #which guarantees that they won't get drawn on top of each other
                    pScore.undraw()
                    pScore=Text(Point(200,600),"players hand value: "+str(startgame.evaluateHand(startgame.getHandP())))
                    pScore.setStyle("bold")
                    pScore.setFill("black")
                    pScore.setSize(37)
                    pScore.draw(myWin)
                    #I also need to update the displayed hand value
                    if startgame.evaluateHand(getHandP())>21:
                        winlose=Text(Point(400,600),"You busted! Dealer wins.")
                        winlose.setStyle("bold")
                        winlose.setFill("black")
                        winlose.setSize(37)
                        winlose.draw(myWin)
            
                        #I'm using the same definition for denoting player busting butt now with an actual purpose after undrawing the dummy
                if StandButton.clicked(pt):
                    startgame.DealerPlays(myWin, 450, 100)
                    dScore.undraw()
                    dScore=Text(Point(200,300),"dealers hand value: ")
                    dScore.setStyle("bold")
                    dScore.setFill("black")
                    dScore.setSize(37)
                    dScore.draw(myWin)
                    #Now it's time to show the dealer's hand value properly
                    if startgame.evaluateHand(startgame.getHandD())>21:
                        winlose=Text(Point(400,600),"dealer busted! You wins.")
                        winlose.setStyle("bold")
                        winlose.setFill("black")
                        winlose.setSize(37)
                        winlose.draw(myWin)
                    elif startgame.evaluateHand(startgame.getHandD())==startgame.evalHand(getHandP()):
                        winlose=Text(Point(400,600),"draw")
                        winlose.setStyle("bold")
                        winlose.setFill("black")
                        winlose.setSize(37)
                        winlose.draw(myWin)
                    elif startgame.evaluateHand(startgame.getHandD())>startgame.evalHand(getHandP()):
                        winlose=Text(Point(400,600),"dealer wins")
                        winlose.setStyle("bold")
                        winlose.setFill("black")
                        winlose.setSize(37)
                        winlose.draw(myWin)
                    else:
                        winlose=Text(Point(400,600),"You win")
                        winlose.setStyle("bold")
                        winlose.setFill("black")
                        winlose.setSize(37)
                        winlose.draw(myWin)

                        
                
            pt=myWin.getMouse()

            

    myWin.close()
        
main()



    

