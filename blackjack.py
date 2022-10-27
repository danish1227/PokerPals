#Imports
from tkinter import Y
from card import Card
from deck import Deck
from player import Player
from chip import Chip
import random

deck = Deck()
dealer = Player("dealer")
me = Player([Chip("Black"), Chip("Blue"), Chip("Green"), Chip("Green"), Chip("red"), Chip("red"), Chip("red"), Chip("white"), Chip("white"), Chip("white"), Chip("white"), Chip("white")])

while True:
    bet = ["white", "white"]#input("What chips are you placing down?(List of chip colors, separated by commas): ").split(", ")
    chips_to_remove = []
    for chip in bet:
        for poker_chip in me.wallet:
            if chip.title() == poker_chip.get_color():
                chips_to_remove.append(poker_chip)
                me.remove_from_wallet(poker_chip)
                break
   
    #deal the dealer their first card
    card = deck.remove_card_to_hand()
    dealer.add_card(card)
    #Show dealer's first card and value
    print("Dealer Hand: ")
    print(dealer.get_hand()[0])
    dealer_value = str(dealer.get_value())

    #deal player first card
    card = deck.remove_card_to_hand()
    me.add_card(card)

    #deal dealer 2nd card
    card = deck.remove_card_to_hand()
    dealer.add_card(card)

    #deal player second card
    card = deck.remove_card_to_hand()
    me.add_card(card)
    print("Player Hand: ")
    for card in me.get_hand():
        print(str(card))
    print()
    print()
    print("Dealer Value: " + dealer_value)
    print("Player Value: " + str(me.get_value()))
    blackjack = False
    out = False
    print()
    while out == False and blackjack != True:
        if me.get_value() < 21:
            hit_ask = input("Hit?: ")
            if hit_ask.lower() != "y":
                out = True
            else:
                card = deck.remove_card_to_hand()
                me.add_card(card)
                print("Player Hand: ")
                for card in me.get_hand():
                    print(str(card))
                print("Player Value: " + str(me.get_value()))
        elif me.get_value() == 21:
            blackjack = True
            print("Blackjack!")
            hit_ask = ""
            out = True
        else:
            print("bust")
            hit_ask = ""
            out = True
            blackjack = False
    while dealer.get_value() < 17:
        if dealer.get_value() > 21:
            print("Dealer Bust")
        elif dealer.get_value() == 21:
            print("Dealer Blackjack")
        else:
            card = deck.remove_card_to_hand()
            dealer.add_card(card)
            print("Dealer Hand: ")
            for card in dealer.get_hand():
                print(str(card))
            print("Dealer Value: " + str(dealer.get_value()))
    print()
    print()
    print("Player Final Value: " + str(me.get_value()))
    print("Dealer Final Value: " + str(dealer.get_value()))
    print()
    print()
    if me.get_value() > 21 and dealer.get_value() > 21:
        print("Push")
    elif me.get_value() > 21 and dealer.get_value() <= 21:
        print("Dealer Win")
    elif me.get_value() <= 21 and dealer.get_value() > 21:
        print("Player Win")
    elif me.get_value() < dealer.get_value():
        print("Dealer Win")
    elif me.get_value() > dealer.get_value():
        print("Player Win")
    break


