from moai import Moai


class Game:
    def __init__(self, player):
        self.player = player
        self.moai = [Moai(1)]
