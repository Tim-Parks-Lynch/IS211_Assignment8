from Player_Class import HumanPlayer
from Game_Class import Game

if __name__ == "__main__":
    p1 = HumanPlayer("Jim")
    p2 = HumanPlayer("Sam")

    pig_game = Game(p1, p2)
    pig_game.play_game()
