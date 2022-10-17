# Think this will be the model
from View_Class import View


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None
        self.current_player = self.players[0]

    def check_winner(self):
        for player in self.players:
            if player.total >= 50:
                self.winner = player
                return True
        return False

    def play_game(self):
        while not self.check_winner():
            self.current_player.turn()
            self.check_winner()
            self.change_player()
        wv.view(self.winner)

    def change_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]


wv = View("Winner").create_view()
