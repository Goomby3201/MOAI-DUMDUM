import json
import os


ACHIVEMENTS_FILE = "achievements.json"

ALL_ENDINGS = {
    "MOAI DESTRUCTION",
    "GUM-GUM PLANET",
    "ECONOMIC COLLAPSE",
    "PEACE"
}

ACHIEVMENTS = {
    "first_gum": {
        "name": "First Taste",
        "description": "Kaufe dein erstes Gum-Gum."
    },
    "first_moai": {
        "name": "DUM-DUM",
        "description": "Lass deinen ersten neuen Moai entstehen"
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
        "description": "Schalte alle Endings frei."
    },
    "all_endings": {
        "name": "I HAVE SEEN EVERYTHING",
        "description": "Schalte alle Endings frei."
    }
}


def load_anchievements():
    if not os.path.exists(ACHIEVEMENTS_FILE):
        return []

    try:
        with open(ACHIEVEMENTS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecoderError:
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
