from player import Player
from game import Game

# Name can be changed later on
player = Player("Larry")
game = Game(player)

print(f"Willkommen, {player.name}!")
print(f"Geld: ${player.money}")
print(f"Moai: {game.moai_count}")
