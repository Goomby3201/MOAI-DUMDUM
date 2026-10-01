class Player:
    def __init__(self, name):
        self.name = name
        self.money = 20
        self.gum_gum = 0

    def buy_gum_gum(self, amount):
        price = amount * 5

        if self.money < price:
            return False

        self.money -= price
        self.gum_gum += amount
        return True
