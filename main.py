from player import Player
from game import Game
from jobs import do_job


player = Player("Larry")
game = Game(player)

print(f"Geld vorher: ${player.money}")

do_job(player, "museum")

print(f"Geld nach dem Job: ${player.money}")
