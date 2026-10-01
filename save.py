import json

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
            return json.load(file)
    except FileNotFoundError:
        return None
