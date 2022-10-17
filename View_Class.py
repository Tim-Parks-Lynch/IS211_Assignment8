class View:
    def __init__(self, view_type):
        self.view_type = view_type

    def __str__(self):
        return f"{self.view_type} View Initalized"

    def create_view(self):
        if self.view_type == "Scratched":
            v = ScratchedView(self.view_type)
            return v
        elif self.view_type == "Held":
            v = HeldView(self.view_type)
            return v
        elif self.view_type == "Rolled":
            v = RolledView(self.view_type)
            return v
        elif self.view_type == "Start":
            v = StartView(self.view_type)
            return v
        elif self.view_type == "Winner":
            v = WinnerView(self.view_type)
            return v


class StartView(View):
    def __init__(self, view_type):
        super().__init__(view_type)

    def view(self):
        print("\n********************************")
        print("*            Pig               *")
        print("*            Game              *")
        print("********************************\n")


class ScratchedView(View):
    def __init__(self, view_type):
        super().__init__(view_type)

    def view(self, name):
        print("\n----------------------------------")
        print(f"{name} rolled a 1:                 ")
        print(f"{name} Scratched -- Switching Users")
        print("----------------------------------\n")


class HeldView(View):
    def __init__(self, view_type):
        super().__init__(view_type)

    def view(self, name):
        print("********************************")
        print(f"{name} Held")
        print("********************************\n")


class RolledView(View):
    def __init__(self, view_type):
        super().__init__(view_type)

    def view(self, name, rolled, turn_total, player_total):
        print(f"\n{name}'s Turn")
        print("----------------------------------")
        print(f"{name} Rolled a {rolled} ")
        print(f"Turn Total = {turn_total}")
        print(f"Possible total if held = {player_total + turn_total}")
        print(f"Player total before holding = {player_total}")
        print("----------------------------------\n\n")


class WinnerView(View):
    def __init__(self, view_type):
        super().__init__(view_type)

    def view(self, player):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"{player.name} Wins!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")


# if __name__ == "__main__":
#     v0 = View("Start").create_view()
#     v0.game_start_view()
#     v1 = View("Scratched").create_view()
#     v2 = View("Held").create_view()
#     v3 = View("Rolled").create_view()
#     v1.player_scratched_view("Jon")
#     v2.player_held_view("Jon")
#     v3.player_rolled_view("Tim", 6, 20, 30)

#     print(v0)
#     print(v1)
#     print(v2)
#     print(v3)
