#imports
from card import Card

if __name__ == "__main__":
    deck = []
    cardNames = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

    for suit in suits:
        for name in cardNames:
            deck.append(Card(name, suit))
    for card in deck:
        print(card)