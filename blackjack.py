#Imports
from tkinter import Y
from card import Card
from deck import Deck
from player import Player
from chip import Chip
import random

#function to deal cards
def deal_card(deck, player):
    card = deck.remove_card()
    player.add_card(card)

#get an amount to bet from the user
def get_player_bet():
    black_chips = int(input("How many black chips do you want to bet?: "))
    blue_chips = int(input("How many blue chips do you want to bet?: "))
    green_chips = int(input("How many green chips do you want to bet?: "))
    red_chips = int(input("How many red chips do you want to bet?: "))
    white_chips = int(input("How many white chips do you want to bet?: "))
    return {"White" : white_chips, "Red" : red_chips, "Green" : green_chips, "Blue" : blue_chips, "Black" : black_chips}

#verify chips being bet are real
def verify_and_subtract_chips(bet, player):
    for bet_chip in bet:
        for chip in player.wallet:
            if bet_chip.title() == chip.title():
                if player.wallet[chip.title()] >= bet[bet_chip.title()]:
                    player.wallet[chip.title()] = player.wallet[chip.title()] - bet[bet_chip.title()]
                else: 
                    print("Not enough " + chip.title() + " poker chips to bet " + str(bet[bet_chip.title()]) + " of them.")

# Start game
chips = [Chip("Black"), Chip("Blue"), Chip("Green"), Chip("red"), Chip("white")]
deck = Deck() 
dealer = Player("dealer")
me = Player({"White" : 1, "Red" :1, "Green" : 1, "Blue" : 1, "Black" : 1})
change_bet = "y"
while True:
    if change_bet[0] == "y":
        print("-----------------------------")
        me.display_chip_money(chips)
        print("-----------------------------")
        bet = get_player_bet()
    me.display_chip_money(chips)
    print()
    #verify player is only betting chips they have and subtract the chips they do have from their wallet
    print("Betting Chips... Your Bet: " + str(bet))
    print()
    verify_and_subtract_chips(bet, me)
    me.display_chip_money(chips)
    print()
    #deal the dealer their first card
    deal_card(deck, dealer)
    #Show dealer's first card and value
    print("-----------------------------")
    print("Dealer Hand: ")
    print(dealer.get_hand()[0])
    print("-----------------------------")
    dealer_value = str(dealer.get_value())

    #deal player first card
    deal_card(deck, me)
    #deal dealer 2nd card
    deal_card(deck, dealer)
    #deal player second card
    deal_card(deck, me)

    print("-----------------------------")
    print("Player Hand: ")
    for card in me.get_hand():
        print(str(card))
    print("-----------------------------")
    print()
    print()
    #compare values
    print("Dealer Value: " + dealer_value)
    print("Player Value: " + str(me.get_value()))
    blackjack = False
    out = False
    print()

    #wait for user input to see if user wants to hit or not
    while out == False and blackjack != True:
        #if player value is below 21 continue 
        if me.get_value() < 21:
            hit_ask = input("Hit?: ")
            #ask user for opt out
            if hit_ask.lower() != "y":
                out = True
            else:
                card = deck.remove_card()
                me.add_card(card)
                print("-----------------------------")
                print("Player Hand: ")
                for card in me.get_hand():
                    print(str(card))
                print("Player Value: " + str(me.get_value()))
                print("-----------------------------")
        #check for user blackjack
        elif me.get_value() == 21:
            blackjack = True
            print("Blackjack!")
            hit_ask = ""
            out = True
        #check for bust-
        else:
            print("bust")
            hit_ask = ""
            out = True
            blackjack = False
    #dealer logic
    while dealer.get_value() < 17:
        #check for dealer bust
        if dealer.get_value() > 21:
            print("Dealer Bust")
        #check for dealer blackjack
        elif dealer.get_value() == 21:
            print("Dealer Blackjack")
        #else keep getting cards
        else:
            card = deck.remove_card()
            dealer.add_card(card)
            print("-----------------------------")
            print("Dealer Hand: ")
            for card in dealer.get_hand():
                print(str(card))
            print("Dealer Value: " + str(dealer.get_value()))
            print("-----------------------------")
    
    #display final values
    print()
    print()
    print("Player Final Value: " + str(me.get_value()))
    print("Dealer Final Value: " + str(dealer.get_value()))
    print()
    print()
    #determine winner and payout
    if me.get_value() > 21 and dealer.get_value() > 21:
        print("Push")
        me.add_wallet(bet)
    elif me.get_value() > 21 and dealer.get_value() <= 21:
        print("Dealer Win")
    elif me.get_value() < 21 and dealer.get_value() > 21:
        print("Player Win")
        chips_to_add = bet.copy()
        for chip in chips_to_add:
            chips_to_add[chip] = chips_to_add[chip]*2
        me.add_wallet(chips_to_add)
    elif me.get_value() < 21 and dealer.get_value() > 21:
        print("Player Win, Blackjack!")
        chips_to_add = bet.copy()
        for chip in chips_to_add:
            chips_to_add[chip] = chips_to_add[chip]*2
        me.add_wallet(chips_to_add)
    elif me.get_value() < dealer.get_value():
        print("Dealer Win")
    elif me.get_value() > dealer.get_value():
        print("Player Win")
        chips_to_add = bet.copy()
        for chip in chips_to_add:
            chips_to_add[chip] = chips_to_add[chip]*2
        me.add_wallet(chips_to_add)
    print()
    me.display_chip_money(chips)
    print()
    #ask to play again
    play = input("Keep Playing?(y/n): ").lower()
    if play[0] != "y":
        break
    else:
        #clear hands and ask if player wants to change their bet
        me.clear_hand()
        dealer.clear_hand()
        change_bet = input("Change Your Bet?(y/n): ").lower()