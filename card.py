class Card:
    def __init__(self, name, suit):
        nameValue = {"Ace" : 11, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
        self.name = name.title()
        self.suit = suit
        self.value = nameValue[self.name]
    def __str__(self):
        return str(self.name) + " of " + self.suit
    def get_value(self):
        return self.value
    def get_suit(self):
        return self.suit
    def set_value(self, value):
        self.value = value