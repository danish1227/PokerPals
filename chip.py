class Chip:
    #constructor
    def __init__(self, color):
        nameValue = {"White" : 1, "Red" : 2, "Green" : 3, "Blue" : 4, "Black" : 5}
        self.color = color.title()
        self.value = nameValue[self.color]
    # tostring method
    def __str__(self):
        return self.color + " : " + str(self.value)
    #getter for a chips value
    def get_value(self):
        return self.value
    #getter for the color of the chip
    def get_color(self):
        return self.color