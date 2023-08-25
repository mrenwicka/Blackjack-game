# Blackjack-game

GUI based program that simulates a game of BlackJack.

An object-oriented Black Jack program with at least three classes that you will define and use. The program randomizes cards that the user picks, as well as the ones that the dealer generates. Program uses card images to simulate real playing cards. Once the player is done drawing, the dealers cards are revealed to see whether or not its a bust or a win.

PlayingCard class - The PlayingCard class is quite simple, just two instance variables, suit and rank. The methods getSuit() and getRank(), are accessor methods. The getRank() method is a hard-coded list of the ranks (from “Ace” to “King”), while the getSuit() method is a hard-coded small dictionary of the suits (for example, mapping “s” to “Spades”, etc.). The ranks and suits are then indexed into the list and the dictionary respectively using the rank and suit attributes. 

Decktest class - The Decktest class is a class that represents a deck of cards. This class imports and uses the PlayingCard class. The only instance variable used for this class is a list of PlayingCard objects, called cardList. 

Blackjack class - The Blackjack class contains functions to initiate a new Blackjack game as well as get hand values, evaluate hands, deal, and hit. It utilizes both of the classes mentioned above to perform these methods. It also uses a button class to created buttons on for hitting, holding, and restarting the game. 

