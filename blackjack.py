#Imports

from card import Card

from deck import Deck

if __name__ == "__main__":
    deck = Deck()

    for card in deck.get_cards():
        print(str(card))