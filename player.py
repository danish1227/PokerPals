from chip import Chip

class Player:
    def __init__(self, wallet):
        self.hand = []
        self.wallet = []
        if wallet != "dealer":
            self.wallet = wallet
        else:
            wallet = "dealer"
        self.value = 0
    def get_hand(self):
        return self.hand
    def get_wallet(self):
        return self.wallet
    def get_value(self):
        return self.value
    def set_wallet(self, wallet):
        self.wallet = wallet
    def add_card(self, card):
        self.hand.append(card)
        self.value += card.get_value()
    def add_wallet(self, chips):
        wallet += chips
    def remove_from_wallet(self, Chip):
        self.wallet.remove(Chip)
    def clear_hand(self):
        self.hand = []

        