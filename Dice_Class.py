from random import randint
from random import seed

seed_num = 0


class Dice:
    def __init__(self):
        self.current_dice_roll = int

    def __str__(self):
        return f"Your roll was {self.current_dice_roll}"

    def roll_dice(self):
        global seed_num
        seed(seed_num)
        self.current_dice_roll = randint(1, 6)
        seed_num += 1

        return self.current_dice_roll
