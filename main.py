from player import Player
from game import Game


player = Player("Larry")
game = Game(player)

player.money = 50
player.buy_gum_gum(9)

for _ in range(9):
    game.feed_moai()

print(f"Moai: {len(game.moai)}")
print(f"Gum-Gum gegeben: {game.gum_gum_given}")
print(f"Weltkontrolle: {game.world_control}%")


