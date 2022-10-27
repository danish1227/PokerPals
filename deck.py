from random import random
from card import Card
import random

class Deck:
    #constructor
    def __init__(self):
        self.cards = []
        #Define names and suits for cards in a deck
        cardNames = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

        #add 52 unique cards ti the deck
        for suit in suits:
            for name in cardNames:
                self.cards.append(Card(name, suit))
    #getter for a deck of cards
    def get_cards(self):
        return self.cards
    #remove 1 card from the deck
    def remove_card(self):
        card = self.cards.pop(random.randrange(len(self.get_cards())))
        return card
        