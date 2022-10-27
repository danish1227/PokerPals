from chip import Chip

class Player:
    #constructor
    def __init__(self, wallet):
        self.hand = []
        self.wallet = []
        #aadd logic for dealer because dealer is the house
        if wallet != "dealer":
            self.wallet = wallet
        else:
            wallet = "dealer"
        self.value = 0
    #getter for a player hand
    def get_hand(self):
        return self.hand
    #getter for a players wallet 
    def get_wallet(self):
        return self.wallet
    #getter for a players card value
    def get_value(self):
        return self.value
    #setter for a new value of the players wallet
    def set_wallet(self, wallet):
        self.wallet = wallet
    #add card to a players hand
    def add_card(self, card):
        self.hand.append(card)
        self.value += card.get_value()
    #add chips to a players hand
    def add_wallet(self, chips):
        wallet += chips
    #remove a chip from the players wallet
    def remove_from_wallet(self, Chip):
        self.wallet.remove(Chip)
    #remove all cards from a players hand
    def clear_hand(self):
        self.hand = []

        