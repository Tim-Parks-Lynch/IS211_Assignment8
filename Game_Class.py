# Think this will be the Controller
from View_Class import View
from datetime import datetime


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None
        self.current_player = self.players[0]

    def check_winner(self):
        for player in self.players:
            if player.total >= 100:
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


class TimedGameProxy(Game):
    def __init__(self, player1, player2, time_limit):
        super().__init__(player1, player2)
        self.start_time = datetime.now()
        self.time_limit = time_limit

    def check_time(self, time_now):
        print("Checking Time")
        return (time_now - self.start_time).total_seconds() > self.time_limit

    def check_winner(self, time_flag):
        print(time_flag)
        if time_flag is False:
            super().check_winner()
        elif time_flag is True:
            print(time_flag)

            self.winner = (
                self.players[0]
                if self.players[0].total > self.players[1].total
                else self.players[1]
            )
            print(self.winner)
            return True

    def play_game(self):
        time_flag = False
        while not self.check_winner(time_flag) and not time_flag:
            self.current_player.turn()
            self.check_winner(time_flag)
            time_flag = self.check_time(datetime.now())
            self.change_player()
            time_flag = self.check_time(datetime.now())
        print(time_flag)
        wv.view(self.winner)
        # if time_flag is False:
        #     return wv.view(self.winner)
        # elif time_flag is True:
        #     if self.players[0].total > self.players[1].total:
        #         return wv.view(self.players[0])
        #     else:
        #         return wv.view(self.players[1])


wv = View("Winner").create_view()
