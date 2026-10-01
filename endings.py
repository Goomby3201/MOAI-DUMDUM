def check_endings(game):
    moai = game.alive_moai_count()

    # Alle Moai zerstört
    if moai == 0:
        return "MOAI DESTRUCTION"

    # Moai übernehmen die Welt
    if game.world_control >= 100:
        return "GUM-GUM PLANET"

    # Pleite und trotzdem Moai-Krise
    if game.player.money == 0 and moai >= 20:
        return "ECONOMIC COLLAPSE"

    # Zu viele Moai
    if moai >= 1000:
        return "MOAI OVERLOAD"

    # Spieler gibt auf
    if game.gum_gum_given == 0 and game.alive_moai_count() == 1:
        return "BORING HUMAN"

    return None
