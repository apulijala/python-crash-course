import random

class Dice():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(random.randint(1, self.sides))


class Lottery():
    def __init__(self, numbers, letters):
        super().__init__()
        self.numbers = numbers
        self.letters = letters

    def draw_lottery(self):
        first = random.choice( self.numbers)
        # print(first)
        second = random.choice(self.numbers)
        third = random.choice(self.letters)
        fourth = random.choice(self.letters)
        return f"{first}{second}{third}{fourth}"

