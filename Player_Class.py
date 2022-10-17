from Dice_Class import Dice
from View_Class import View


# Think this will be the controller
class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def __str__(self):
        return f"{self.name}'s Total = {self.total}"

    def show(self):
        print(f"{self}")

    def turn(self):
        pass


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.dice = (
            Dice()
        )  # This might be an issue later, not really random if they both start off at seed 0

    def turn(self):
        turn_total = 0
        roll_or_hold = None

        while roll_or_hold != "h":
            roll = self.dice.roll_dice()

            if roll > 1:
                turn_total += roll
                rolled_view.view(self.name, roll, turn_total, self.total)
                roll_or_hold = input("Roll(r) or Hold(h) ? ").lower()
            else:
                turn_total = 0
                scratched_view.view(self.name)
                break

        if roll_or_hold == "h":
            self.total += turn_total
            held_view.view(self.name)


start_view = View("Start").create_view()
scratched_view = View("Scratched").create_view()
held_view = View("Held").create_view()
rolled_view = View("Rolled").create_view()
