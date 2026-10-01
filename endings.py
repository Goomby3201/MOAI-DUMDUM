def check_endings(game):
    if game.alive_moai_count() == 0:
        return "MOAI DESTRUCTION"

    if game.world_control >= 100:
        return "GUM-GUM PLANET"

    return None
