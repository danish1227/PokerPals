from chip import Chip

class Player:
    #constructor
    def __init__(self, wallet):
        self.hand = []
        self.wallet = {}
        #aadd logic for dealer because dealer is the house
        if wallet != "dealer":
            self.wallet = wallet
        else:
            wallet = "dealer"
        self.value = 0
        self.money = 0
    #getter for a player hand
    def get_hand(self):
        return self.hand
    #getter for a players wallet 
    def get_wallet(self):
        return self.wallet
    #getter for a players card value
    def get_value(self):
        return self.value
    #get money by calculating  with wallet
    def get_money(self, chips):
        self.money = 0
        for chip in chips:
            for player_chip in self.wallet:
                if chip.get_color() == player_chip:
                    self.money += (self.wallet[player_chip]*chip.get_value())
        return self.money
    #setter for a new value of the players wallet
    def set_wallet(self, wallet):
        self.wallet = wallet
    #add card to a players hand
    def add_card(self, card):
        self.hand.append(card)
        print("Card Value: " + str(card.get_value()))
        possible_value = self.value + card.get_value()
        if "Ace" in [card.name for card in self.hand] and possible_value > 21:
            for card in self.hand:
                if card.name == "Ace" and card.value == 11:
                    card.set_value(1)
                    break
        print("Card Value: " + str(card.get_value()))
        self.value += card.get_value()
    #add chips to a players hand
    def add_wallet(self, chips_amount):
        for chip in chips_amount:
            self.wallet[chip] = self.wallet[chip] + chips_amount[chip]
    #remove a chip from the players wallet
    def remove_from_wallet(self, chips_amount):
        for chip in chips_amount:
            self.wallet[chip] = self.wallet[chip] - chips_amount[chip]
    #remove all cards from a players hand
    def clear_hand(self):
        self.hand = []
        self.value = 0
    def display_chip_money(self, chips):
        if self.wallet != "dealer":
            msg = "My Chip Count: " + str(self.get_wallet()) + "\n" + "My Money: " + str(self.get_money(chips))
            print(msg)
        else:
            print("Player is the Dealer")

        