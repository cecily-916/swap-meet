
class Item:

    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return ("Mint!")
        if self.condition == 4:
            return ("It's great!")
        if self.condition == 3:
            return ("It's ok.")
        if self.condition == 2:
            return ("Not perfect but not broken.")
        if self.condition == 1:
            return ("Not the worst if you're a glass half full sort of person.")
        if self.condition == 0:
            return ("The worst no matter how you look at it.")