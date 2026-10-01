from player import Player
from game import Game


player = Player("Larry")
game = Game(player)

player.money = 50
player.buy_gum_gum(3)

for _ in range(3):
    game.feed_moai()

print(f"Moai: {len(game.moai)}")

game.destroy_moai(1)

print(f"Moai #1 alive: {game.moai[0].alive}")
