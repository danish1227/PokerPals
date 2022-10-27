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
   


