from random import random
from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        cardNames = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

        for suit in suits:
            for name in cardNames:
                self.cards.append(Card(name, suit))

    def get_cards(self):
        return self.cards
    def remove_card_to_hand(self):
        card = self.cards.pop(random.randrange(len(self.get_cards())))
        return card
        