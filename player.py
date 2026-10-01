class Player:
    def __init__(self, name):
        self.name = name
        self.money = 20
        self.gum_gum = 0

    def buy_gum_gum(self, amount, gum_price):
        price = amount * gum_price

        if self.money < price:
            return False

        self.money -= price
        self.gum_gum += amount
        return True
