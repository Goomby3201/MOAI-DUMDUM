import json
import os


ACHIEVEMENTS_FILE = "achievements.json"


ACHIEVEMENTS = {
    "first_gum": {
        "name": "FIRST TASTE",
        "description": "Kaufe dein erstes Gum-Gum."
    },

    "first_moai": {
        "name": "DUM-DUM",
        "description": "Lass deinen ersten neuen Moai entstehen."
    },

    "1000_moai": {
        "name": "MOAI ARMY",
        "description": "Habe 1000 lebende Moai."
    },

    "bulk_buyer": {
        "name": "BULK ORDER",
        "description": "Kaufe 100 Gum-Gum auf einmal."
    },

    "first_destruction": {
        "name": "WHY",
        "description": "Zerstöre deinen ersten Moai."
    },

    "poor_larry": {
        "name": "BROKE",
        "description": "Habe genau $0."
    },

    "almost_broke": {
        "name": "ONE DOLLAR",
        "description": "Habe genau $1."
    },

    "gum_gum_hoarder": {
        "name": "GUM-GUM HOARDER",
        "description": "Habe 100 Gum-Gum gleichzeitig."
    },

    "moai_100": {
        "name": "MOAI PROBLEM",
        "description": "Habe 100 lebende Moai."
    },

    "moai_500": {
        "name": "WHY ARE THERE SO MANY",
        "description": "Habe 500 lebende Moai."
    },

    "bad_investment": {
        "name": "BAD INVESTMENT",
        "description": "Gib dein gesamtes Geld für Gum-Gum aus."
    },

    "boring_human": {
        "name": "BORING HUMAN",
        "description": "Beende ein Spiel, ohne Gum-Gum zu geben."
    },

    "all_endings": {
        "name": "I HAVE SEEN EVERYTHING",
        "description": "Schalte alle Endings frei."
    }
}


ALL_ENDINGS = {
    "MOAI DESTRUCTION",
    "GUM-GUM PLANET",
    "ECONOMIC COLLAPSE",
    "MOAI OVERLOAD",
    "BORING HUMAN"
}


def load_achievements():
    if not os.path.exists(ACHIEVEMENTS_FILE):
        return []

    try:
        with open(ACHIEVEMENTS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_achievements(unlocked):
    with open(ACHIEVEMENTS_FILE, "w") as file:
        json.dump(unlocked, file, indent=4)


def unlock_achievement(achievement_id):
    unlocked = load_achievements()

    if achievement_id in unlocked:
        return False

    unlocked.append(achievement_id)
    save_achievements(unlocked)

    achievement = ACHIEVEMENTS[achievement_id]

    print()
    print("=== ACHIEVEMENT UNLOCKED ===")
    print(f"{achievement['name']}")
    print(f"{achievement['description']}")
    print()

    return True


def check_achievements(game):
    player = game.player
    moai_count = game.alive_moai_count()

    # Geld
    if player.money == 0:
        unlock_achievement("poor_larry")

    if player.money == 1:
        unlock_achievement("almost_broke")

    # Gum-Gum
    if player.gum_gum >= 100:
        unlock_achievement("gum_gum_hoarder")

    # Moai
    if moai_count >= 100:
        unlock_achievement("moai_100")

    if moai_count >= 500:
        unlock_achievement("moai_500")

    if moai_count >= 1000:
        unlock_achievement("1000_moai")


def register_ending(ending):
    unlocked = load_achievements()

    ending_key = f"ending:{ending}"

    if ending_key not in unlocked:
        unlocked.append(ending_key)
        save_achievements(unlocked)

    unlocked_endings = {
        achievement.replace("ending:", "")
        for achievement in unlocked
        if achievement.startswith("ending:")
    }

    if ALL_ENDINGS.issubset(unlocked_endings):
        unlock_achievement("all_endings")


def show_achievements():
    unlocked = load_achievements()

    print("\n=== ACHIEVEMENTS ===")

    for achievement_id, achievement in ACHIEVEMENTS.items():
        if achievement_id in unlocked:
            status = "✓"
        else:
            status = "?"

        print(f"{status} {achievement['name']} - {achievement['description']}")

def register_ending(ending):
    ending_key = f"ending:{ending}"
    unlocked = load_achievements()

    if ending_key not in unlocked:
        unlocked.append(ending_key)
        save_achievements(unlocked)

    unlocked_endings = {
        achievement.replace("ending:", "")
        for achievement in unlocked
        if achievement.startswith("ending:")
    }

    if ALL_ENDINGS.issubset(unlocked_endings):
        unlock_achievement("all_endings")
