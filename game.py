from moai import Moai


class Game:
    def __init__(self, player):
        self.player = player
        self.moai = [Moai(1)]
        self.gum_gum_given = 0
        self.world_control = 0

    def feed_moai(self):
        if self.player.gum_gum <= 0:
            return False

        self.player.gum_gum -= 1
        self.gum_gum_given += 1

        new_moai_id = len(self.moai) + 1
        self.moai.append(Moai(new_moai_id))

        if self.gum_gum_given % 3 == 0:
            self.world_control += 5

        return True

    def destroy_moai(self, moai_id):
        for moai in self.moai:
            if moai.id == moai_id and moai.alive:
                moai.destroy()
                return True

        return False

    def alive_moai_count(self):
        return sum(1 for moai in self.moai if moai.alive)

    def get_gum_price(self):
        return 5 + self.alive_moai_count() - 1

    def get_region(self):
        if self.world_control < 20:
            return "Museum"
        elif self.world_control < 40:
            return "Stadt"
        elif self.world_control < 60:
            return "Land"
        elif self.world_control < 80:
            return "Kontinent"
        elif self.world_control < 100:
            return "Welt"
        else:
            return "MOAI-PLANET"
