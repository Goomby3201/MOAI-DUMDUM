import json

from player import Player
from game import Game
from moai import Moai


SAVE_FILE = "save.json"


def save_game(game):
    data = {
        "player": {
            "name": game.player.name,
            "money": game.player.money,
            "gum_gum": game.player.gum_gum
        },
        "game": {
            "gum_gum_given": game.gum_gum_given,
            "world_control": game.world_control,
            "moai": [
                {
                    "id": moai.id,
                    "alive": moai.alive
                }
                for moai in game.moai
            ]
        }
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_game():
    try:
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    player_data = data["player"]
    game_data = data["game"]

    player = Player(player_data["name"])
    player.money = player_data["money"]
    player.gum_gum = player_data["gum_gum"]

    game = Game(player)
    game.gum_gum_given = game_data["gum_gum_given"]
    game.world_control = game_data["world_control"]

    game.moai = []

    for moai_data in game_data["moai"]:
        moai = Moai(moai_data["id"])
        moai.alive = moai_data["alive"]
        game.moai.append(moai)

    return game
