from player import Player
from game import Game

# Name can be changed later on
player = Player("Larry")
game = Game(player)

print("DUM-DUM: GUM-GUM")
print()

print(f"Geld: ${player.money}")

if player.buy_gum_gum(2):
    print("Du hast 2 Gum-Gum gekauft!")
else:
    print("Du hast nicht genug Geld")

print(f"Geld: ${player.money}")
print(f"Gum-Gum: {player.gum_gum}")
