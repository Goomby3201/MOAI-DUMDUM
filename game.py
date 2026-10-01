from moai import Moai


class Game:
    def __init__(self, player):
        self.player = player
        self.moai = [Moai(1)]

    def feed_moai(self):
        if self.player.gum_gum <= 0:
            return False

        self.player.gum_gum -= 1

        new_moai_id = len(self.moai) + 1
        self.moai.append(Moai(new_moai_id))

        return True
