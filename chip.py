class Chip:
    def __init__(self, color):
        nameValue = {"White" : 1, "Red" : 2, "Green" : 3, "Blue" : 4, "Black" : 5}
        self.color = color.title()
        self.value = nameValue[self.color]
    
    def get_value(self):
        return self.value

    def get_color(self):
        return self.color