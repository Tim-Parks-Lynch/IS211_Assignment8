from Player_Class import HumanPlayer
from Player_Class import ComputerPlayer
from Game_Class import Game
from Game_Class import TimedGameProxy


def make_player(player_type, player_name):
    """
    Factory Function
    :param player_type:
    :param player_name:
    :return:
    """

    if player_type.upper() == "C":
        return ComputerPlayer(player_name)
    elif player_type.upper() == "H":
        return HumanPlayer(player_name)
    else:
        raise ValueError("Human(H) or Computer(C) players only")


def make_game(player_one, player_two, timed_bool, time_limit=60):
    if timed_bool.upper() == "Y":
        return TimedGameProxy(player_one, player_two, time_limit)
    elif timed_bool.upper() == "N":
        return Game(player_one, player_two)
    else:
        raise ValueError(
            "Timed Games or Untimed Games only. Please specify Y/N for timed game?"
        )


if __name__ == "__main__":
    p1 = HumanPlayer("Jim")
    p2 = ComputerPlayer("Sam")

    pig_game = make_game(p1, p2, "Y", 60)
    pig_game.play_game()
