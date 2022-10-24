from Player_Class import HumanPlayer
from Player_Class import ComputerPlayer
from Game_Class import Game
from Game_Class import TimedGameProxy
from View_Class import View
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--player1",
        help="Human(H) or Computer(C) player",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--player2",
        help="Human(H) or Computer(C) player",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--timed",
        help="Y for timed game, N for untimed game",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    sv = View("Start").create_view()
    sv.view()

    player1_name = input("Player 1's name please: ")
    player2_name = input("Player 2's name please: ")

    p1 = make_player(args.player1, player1_name)
    p2 = make_player(args.player2, player2_name)

    timed_game_amount = None

    if args.timed.upper() == "Y":
        timed_game_amount = int(
            input("How many seconds would you like to play for ? ")
        )

    pig_game = make_game(p1, p2, args.timed.upper(), timed_game_amount)
    pig_game.play_game()
