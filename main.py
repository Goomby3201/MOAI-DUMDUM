from player import Player
from game import Game

# Name can be changed later on
player = Player("Larry")
game = Game(player)

player.buy_gum_gum(2)

print(f"Gum-Gum: {player.gum_gum}")
print(f"Moai: {len(game.moai)}")

game.feed_moai()

print("Nach dem Fütteren:")
print(f"Gum-Gum: {player.gum_gum}")
print(f"Moai: {len(game.moai)}")

