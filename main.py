from player import Player
from game import Game

# Name can be changed later on
player = Player("Larry")
game = Game(player)

print("DUM-DUM: GUM-GUM")
print()

print(f"Geld: ${player.money}")
print(f"Moai: {len(game.moai)}")
print(f"Erster Moai: #{game.moai[0].id}")
