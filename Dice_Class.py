from random import randint
from random import seed


class Dice:
    def __init__(self):
        self.seed = 0
        self.current_dice_roll = int

    def __str__(self):
        return f"Your roll was {self.current_dice_roll}"

    def roll_dice(self):
        seed(self.seed)
        self.current_dice_roll = randint(1, 6)
        self.seed += 1

        return self.current_dice_roll
